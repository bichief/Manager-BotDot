from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_statuses(pk):
    allowed_statuses = ['Связь', 'ТЗ', 'Оплата', 'Оплачено', 'Разработка', 'Готово', 'Отказ', 'Думает']

    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text=f'{allowed_statuses[0]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[0]}'),
                                            InlineKeyboardButton(text=f'{allowed_statuses[1]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[1]}'),
                                            InlineKeyboardButton(text=f'{allowed_statuses[2]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[2]}')
                                        ],
                                        [
                                            InlineKeyboardButton(text=f'{allowed_statuses[3]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[3]}'),
                                            InlineKeyboardButton(text=f'{allowed_statuses[4]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[4]}'),
                                            InlineKeyboardButton(text=f'{allowed_statuses[5]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[5]}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='----------------', callback_data='empty')
                                        ],
                                        [
                                            InlineKeyboardButton(text=f'{allowed_statuses[7]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[7]}'),
                                            InlineKeyboardButton(text=f'{allowed_statuses[6]}',
                                                                 callback_data=f'set_{pk}_{allowed_statuses[6]}')
                                        ],
                                        [
                                            InlineKeyboardButton(text='⬅ Назад', callback_data=f'client_{pk}')
                                        ]
                                    ])
    return keyboard
