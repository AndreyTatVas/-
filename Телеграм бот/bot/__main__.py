import os
import asyncio
import logging

from aiogram import Dispatcher, Bot

from bot.commands import register_user_commands


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    db = Dispatcher()
    bot = Bot(token=os.getenv('token'))

    register_user_commands(db)

    await db.start_polling(bot)


if __name__ == '__main__':

    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
