from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.clients_manager_kb import client_manager_show
from loader import dp
from utils.db_api.db_commands import get_is_working


@dp.callback_query_handler(Text(equals='my_clients'))
async def show_clients_manager(call: types.CallbackQuery):
    state = await get_is_working(call.from_user.id)
    if state:
        keyboard = await client_manager_show(call.from_user.id)
        if len(keyboard.inline_keyboard) == 1:
            await call.answer('Список клиентов отсутствует.', show_alert=True)
        else:
            await call.message.edit_text('Ниже представлен список клиентов, которые относятся к тебе.',
                                         reply_markup=keyboard)
    else:
        await call.answer('Твоя рабочая смена еще не начата!\n'
                          'Нажми на кнопку "Начать работу"', show_alert=True)
