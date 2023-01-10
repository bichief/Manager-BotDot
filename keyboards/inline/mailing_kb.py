from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def kb_mailing(url, name):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text=f'{name}', url=url)
                                        ]
                                    ])

    return keyboard