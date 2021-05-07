import os
import sys
import logging

from aiogram import Bot, types # Dispatcher, executor, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, ChatActions

from views import OpenWeather

# token from telegram bot
API_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

Api = OpenWeather()

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    Typing '/help' displays a text message.
    """
    await message.reply('Hi!\nIm OpenWeatherBot.\n'
                        'Enter the name of the city or country.')

@dp.message_handler(commands=['start'])
    """
    Typing '/start' displays a text message.
    """
async def process_start_command(message: types.Message):
    await message.reply('Hi!\nИспользуй /help, '
                        'чтобы узнать список доступных команд!')

@dp.message_handler()
async def weather_bot(message: types.Message):
    response = Api.main_response(message.text)
    await bot.send_photo(message.from_user.id, response[0],
                         response[1], disable_notification=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
