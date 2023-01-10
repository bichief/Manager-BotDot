from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data import config
from keyboards.inline.mailing_kb import kb_mailing
from loader import dp
from states import GetMailing


@dp.message_handler(Command('mail'), user_id=config.admins)
async def start_mailing(message: types.Message):
    await message.answer('Отправь мне сообщение для отправления в чат.\n'
                         'Чтобы отправить с клавиатурой, отправь форму:\n\n'
                         'Текст&name&url')
    await GetMailing.mail.set()


@dp.message_handler(state=GetMailing.mail)
async def send_mailing(message: types.Message, state: FSMContext):
    text = message.text
    await state.reset_state(True)

    if '&' in text:
        array_text = text.split('&')

        keyboard = await kb_mailing(url=array_text[2], name=array_text[1])

        await dp.bot.send_message(
            chat_id=-1001819321483,
            text=array_text[0],
            reply_markup=keyboard
        )
    else:
        await dp.bot.send_message(
            chat_id=-1001819321483,
            text=text
        )


@dp.message_handler(Command('ch'), user_id=config.admins)
async def channel_mailing(message: types.Message):
    await message.answer('Отправь мне сообщение для отправления в канал\n'
                         'Чтобы отправить с клавиатурой, отправь форму:\n\n'
                         'Текст|name|url')
    await GetMailing.channel.set()


@dp.message_handler(state=GetMailing.channel)
async def post_channel(message: types.Message, state: FSMContext):
    text = message.text
    keyboard = await kb_mailing(url=text.split('|')[2], name=text.split('|')[1])
    await message.bot.send_message(
        chat_id=-1001820253462,
        text=text.split('|')[0],
        reply_markup=keyboard
    )
    await state.reset_state(True)