from aiogram import types

from keyboards.inline.manager_action import action_for_manager
from loader import dp
from utils.db_api.db_commands import create_client, get_client


@dp.message_handler(user_id=5555350071)
async def get_vote(message: types.Message):
    data = message.text.split('\n')

    status = await create_client(name=data[1], phone=data[0])
    await message.answer('+')

    client = await get_client(phone=data[0])
    if status:
        pass
    else:
        await dp.bot.send_message(
            chat_id=-1001819321483,
            text='😱 <b> Новая заявка!</b>\n'
                 'Информация о клиенте:\n'
                 f'Имя: {client.name}\n'
                 f'Номер: {client.phone}\n\n'
                 f'Telegram: <a href="https://t.me/{client.phone}"> нажми </a>\n'
                 f'WhatsApp: <a href="https://api.whatsapp.com/send?phone={client.phone[1:]}"> нажми </a>\n\n'
                 f'Статус: {client.status}\n'
                 f'Доп. инфа: {"Отсутствует" if client.information is None else client.information}',
            disable_web_page_preview=True,
            reply_markup=await action_for_manager(client_id=client.id)
        )
