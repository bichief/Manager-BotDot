from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

num = ReplyKeyboardMarkup(resize_keyboard=True,
                          keyboard=[
                              [
                                  KeyboardButton(text='Показать номер', request_contact=True)
                              ]
                          ])
