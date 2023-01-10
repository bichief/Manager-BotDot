from aiogram import types

from data.config import admins
from keyboards.inline.choose_action import action
from loader import dp


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def get_contact(message: types.Message):
    number = message.contact.phone_number

    await message.answer('Отлично!\n'
                         'Я записал тебя как менеджера, но еще необходимо дождаться одобрения заявки.\n\n'
                         'Как только её одобрят - уведомлю об этом. Спасибо.',
                         reply_markup=types.ReplyKeyboardRemove())

    keyboard = await action(telegram_id=message.chat.id, username=message.from_user.username, phone=number,
                            name=message.from_user.first_name)
    await dp.bot.send_message(
        chat_id=admins[0],
        text='Пришла новая заявка от менеджера.\n\n'
             f'Имя: {message.from_user.first_name}\n'
             f'Юзернейм: {message.from_user.username}\n'
             f'Номер: {number}\n\n'
             f'Выберите действие на клавиатуре.',
        reply_markup=keyboard
    )
