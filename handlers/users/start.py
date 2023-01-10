from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from keyboards.default.get_number import num
from keyboards.inline.main_menu import menu
from loader import dp
from utils.db_api.db_commands import select_manager


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    manager = await select_manager(telegram_id=message.chat.id)
    if len(manager) != 0:
        keyboard = await menu(telegram_id=message.chat.id)
        await message.answer('Добро пожаловать в главное меню!', reply_markup=keyboard)
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!\n\n"
                             f"Нажми на кнопку ниже, чтобы оставить свой номер.", reply_markup=num)


@dp.callback_query_handler(Text(equals='menu'))
async def go_menu(call: types.CallbackQuery):
    keyboard = await menu(telegram_id=call.from_user.id)
    await call.message.edit_text('Добро пожаловать в главное меню!', reply_markup=keyboard)
