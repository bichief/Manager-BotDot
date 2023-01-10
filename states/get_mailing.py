from aiogram.dispatcher.filters.state import StatesGroup, State


class GetMailing(StatesGroup):
    mail = State()
    channel = State()