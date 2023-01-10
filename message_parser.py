from telethon import TelegramClient

from data.config import api_id, api_hash
from utils.db_api.db_commands import get_last_client


async def parse_votes():
    client = TelegramClient('parser', api_id, api_hash)
    await client.connect()
    channel_username = '@TildaFormsBot'
    last_client = await get_last_client()

    for message in await client.get_messages(channel_username, limit=1):
        msg = message.message.split('\n')

        text = f'{msg[1][7:]}\n' \
               f'{msg[2][5:]}'
        try:
            if last_client.phone == msg[1][7:]:
                await client.disconnect()
            else:
                await client.send_message('@ManagerDotBot', text)
                await client.disconnect()
        except AttributeError:
            await client.disconnect()
