from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import status_manager


async def menu(telegram_id):
    main_menu = InlineKeyboardMarkup(row_width=3)

    status = await status_manager(telegram_id)

    if status.is_working is True:
        stop_btn = InlineKeyboardButton(text='🔴 Завершить работу', callback_data=f'stop_{telegram_id}')
        main_menu.add(stop_btn)
    else:
        start_btn = InlineKeyboardButton(text='🟢 Начать работу', callback_data=f'start_{telegram_id}')
        main_menu.add(start_btn)

    clients_btn = InlineKeyboardButton(text='Мои клиенты', callback_data='my_clients')
    good_info = InlineKeyboardButton(text='Notion',
                                     url='https://www.notion.so/invite/2b2f6b6a27f3d278520578b4a9ea43fad4ff3e12')
    chat_link = InlineKeyboardButton(text='Чат', url='https://t.me/+tlogYb4mW9k5ZWUy')

    main_menu.add(clients_btn)
    main_menu.add(good_info, chat_link)

    return main_menu
