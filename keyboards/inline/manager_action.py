from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def action_for_manager(client_id):
    action = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='💡 Беру', callback_data=f'take_{client_id}')
                                      ]
                                  ])

    return action
