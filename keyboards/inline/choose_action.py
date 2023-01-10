from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def action(telegram_id, username, phone, name):
    choose = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Подтвердить',
                                                               callback_data=f'accept|{telegram_id}|{username}|{phone}|{name}'),
                                          InlineKeyboardButton(text='Отказать', callback_data=f'deny|{telegram_id}')
                                      ]
                                  ])

    return choose
