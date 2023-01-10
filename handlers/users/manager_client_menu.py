import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.manager_clients import show_clients_manager
from handlers.users.start import bot_start
from keyboards.inline.manager_client_menu_kb import edit_client
from keyboards.inline.statuses import show_statuses
from loader import dp
from states import GetInfo
from utils.db_api.db_commands import get_client_pk, update_status_client, update_info_client, update_manager_client


@dp.callback_query_handler(Text(startswith='client_'))
async def client_profile(call: types.CallbackQuery):
    client = await get_client_pk(pk=call.data.split('_')[1])
    keyboard = await edit_client(pk=call.data.split('_')[1])
    await call.message.edit_text(f'🕵️‍♂️<b>Информация о клиенте №{call.data.split("_")[1]}</b>\n\n'
                                 f'🧑‍💼Имя: <b>{client.name}</b>\n'
                                 f'📲Номер: <code>{client.phone}</code>\n\n'
                                 f'🔵Telegram: <a href="https://t.me/{client.phone}"> нажми </a>\n'
                                 f'🟢WhatsApp: <a href="https://api.whatsapp.com/send?phone={client.phone[1:]}"> нажми </a>\n\n'
                                 f'📊Статус: <b>{client.status}</b>\n'
                                 f'ℹ️Доп. инфа: <b>{"Отсутствует" if client.information is None else client.information}</b>',
                                 reply_markup=keyboard,
                                 disable_web_page_preview=True
                                 )


@dp.callback_query_handler(Text(startswith='edit_status_'))
async def edit_client_status(call: types.CallbackQuery):
    pk = call.data.split('_')[2]
    keyboard = await show_statuses(pk=pk)
    await call.message.edit_text('Выбери необходимый статус для клиента.', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='set_'))
async def set_status_client(call: types.CallbackQuery):
    pk = call.data.split('_')[1]
    status = call.data.split('_')[2]
    await update_status_client(pk=pk, status=status)
    await call.answer(f'Статус клиента №{pk}\n'
                      f'Был успешно изменен на:\n'
                      f'{status}', show_alert=True)
    await client_profile(call=call)


@dp.callback_query_handler(Text(startswith='info_'))
async def edit_info_client(call: types.CallbackQuery):
    pk = call.data.split('_')[1]
    message = await call.message.answer('Отправь мне доп. инфу по клиенту.')
    await GetInfo.info.set()

    state = dp.current_state(user=call.from_user.id)
    await state.update_data(
        {
            'message_id': message.message_id,
            'pk': pk,
            'call': call
        }
    )


@dp.message_handler(state=GetInfo.info)
async def get_info_client(message: types.Message, state: FSMContext):
    info = message.text

    data = await state.get_data()
    pk = data.get('pk')
    call = data.get('call')
    await update_info_client(pk=data.get('pk'), info=info)
    await message.delete()

    await dp.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=data.get('message_id'),
        text='Информация успешно обновлена!'
    )
    await client_profile(call=call)
    await asyncio.sleep(1.5)

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=data.get('message_id')
    )

    await state.reset_state(True)


@dp.callback_query_handler(Text(startswith='edit_close_'))
async def close_client(call: types.CallbackQuery):
    pk = call.data.split('_')[2]
    await update_manager_client(pk=pk)
    await call.answer('Сделка успешно закрыта!', show_alert=True)
    await bot_start(message=call.message)
