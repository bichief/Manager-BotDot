from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from utils.db_api.db_commands import update_client_manager


@dp.callback_query_handler(Text(startswith='take'), chat_id=-1001819321483)
async def take_client(call: types.CallbackQuery):
    data = call.data.split('_')

    await update_client_manager(client_id=data[1], manager_tg_id=call.from_user.id)

    await call.message.edit_text(f'✅ Клиента под номером {data[1]} забрал(-а) @{call.from_user.username}')
