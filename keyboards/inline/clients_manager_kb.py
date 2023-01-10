from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import select_clients_by_manager


async def client_manager_show(manager_tg_id):
    keyboard = InlineKeyboardMarkup(row_width=3)

    data = await select_clients_by_manager(telegram_id=manager_tg_id)

    for row in data:
        btn = InlineKeyboardButton(text=f'{row.name} - {row.status}', callback_data=f'client_{row.pk}')
        keyboard.add(btn)

    back = InlineKeyboardButton(text='⬅️ В меню', callback_data='menu')
    keyboard.add(back)
    return keyboard
