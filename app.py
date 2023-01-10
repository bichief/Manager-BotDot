import asyncio
import os

import aioschedule
import django


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify

    await on_startup_notify(dp)


async def scheduler():
    aioschedule.every(1).minutes.do(parse_votes)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        'admin_panel.admin_panel.settings'
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()

    from message_parser import parse_votes

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())

    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
