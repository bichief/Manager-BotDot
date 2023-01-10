from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.main_menu import menu
from loader import dp
from utils.db_api.db_commands import update_status_manager


@dp.callback_query_handler(Text(startswith='start_'))
async def start_work(call: types.CallbackQuery):
    manager_tg_id = call.data.split('_')[1]
    await update_status_manager(telegram_id=manager_tg_id, status=True)
    await call.answer('Смена успешно начата!')

    keyboard = await menu(telegram_id=manager_tg_id)
    await call.message.edit_text('Добро пожаловать в главное меню!', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='stop_'))
async def stop_work(call: types.CallbackQuery):
    manager_tg_id = call.data.split('_')[1]
    await update_status_manager(telegram_id=manager_tg_id, status=False)
    await call.answer('Смена успешно завершена!')

    keyboard = await menu(telegram_id=manager_tg_id)
    await call.message.edit_text('Добро пожаловать в главное меню!', reply_markup=keyboard)
