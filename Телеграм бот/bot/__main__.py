import os
import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from bot.commands import register_user_commands
from bot.commands.bot_commands import bot_commands


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = [BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands]

    db = Dispatcher()
    bot = Bot(token=os.getenv('token'))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(db)

    await db.start_polling(bot)


if __name__ == '__main__':

    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
