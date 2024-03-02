"""
run.py - Starting file to launch the OpenWeatherBot Telegram bot.

This script initializes the bot and launches it using the aiogram module.
"""
import os
import sys
import logging

import asyncio
from aiogram import Bot
from aiogram import Dispatcher

from src import router as main_router

# Bot token can be obtained via https://t.me/BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

# All handlers should be attached to the Dispatcher
dp = Dispatcher()

async def main() -> None:
    # Initialize Router
    dp.include_router(main_router)

    # Initialize Bot
    bot = Bot(BOT_TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
