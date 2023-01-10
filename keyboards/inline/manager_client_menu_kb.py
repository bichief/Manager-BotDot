from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def edit_client(pk):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Изменить статус',
                                                                 callback_data=f'edit_status_{pk}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Изменить доп. инфо.',
                                                                 callback_data=f'info_{pk}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Закрыть сделку',
                                                                 callback_data=f'edit_close_{pk}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='⬅ Назад', callback_data=f'my_clients')
                                        ]
                                    ])
    return keyboard
