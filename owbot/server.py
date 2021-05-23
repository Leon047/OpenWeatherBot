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
from keyboards import help_btn, weather_items_btn

# token from telegram bot
API_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ...
Api = OpenWeather()


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply('Hi!\nIm OpenWeatherBot.\n'
                        'Enter the name of the city or country.',
                        reply_markup=help_btn)

@dp.message_handler(commands=['main'])
async def send_welcome(message: types.Message):
    await message.reply(Api.weather_item('main'))

@dp.message_handler(commands=['clouds'])
async def send_welcome(message: types.Message):
    await message.reply(Api.weather_item('clouds'))

@dp.message_handler(commands=['sys'])
async def send_welcome(message: types.Message):
    await message.reply(Api.weather_item('sys'))

@dp.message_handler(commands=['coord'])
async def send_welcome(message: types.Message):
    await message.reply(Api.weather_item('coord'))

@dp.message_handler()
async def weather_main(message: types.Message):
    response = Api.main_request(message.text)
    await bot.send_photo(message.from_user.id, response[0], response[1],
        disable_notification=True, reply_markup=weather_items_btn
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
