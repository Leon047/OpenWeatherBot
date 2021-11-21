import os
import sys
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.utils.markdown import text

from models import OpenWeather
from keyboards import help_btn, weather_items_btn

# token from telegram bot
API_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure logging debug mod
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# An instance of the class for OpenWeather api.
Api = OpenWeather()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        'Hi! 😁\n'
        'Im OpenWeather bot\n'
        'Enter the name of the city or country.\n'
        'And get the weather forecast.'
    )

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """Help request handler"""
    await message.reply('Hi!\nIm OpenWeather bot.\n'
                        'Get the weather forecast.\n'
                        'Enter the name of the city or country.\n'
                        'Or select the suggested options.',
                        reply_markup=help_btn)

@dp.message_handler(commands=['main'])
async def send_welcome(message: types.Message):
    """Main button handler"""
    await message.reply(Api.weather_item('main'))

@dp.message_handler(commands=['clouds'])
async def send_welcome(message: types.Message):
    """Clouds button handler"""
    await message.reply(Api.weather_item('clouds'))

@dp.message_handler(commands=['sys'])
async def send_welcome(message: types.Message):
    """Sys button handler"""
    await message.reply(Api.weather_item('sys'))

@dp.message_handler(commands=['coord'])
async def send_welcome(message: types.Message):
    """Coord button handler"""
    await message.reply(Api.weather_item('coord'))

@dp.message_handler()
async def weather_main(message: types.Message):
    """Main request handler
    It takes the name of a country or city and returns a weather forecast.
    """
    response = Api.main_request(message.text)
    if response[0] == '404':
        await bot.send_photo(message.from_user.id, response[1], response[2])
    else:
        await bot.send_photo(message.from_user.id, response[0], response[1],
            disable_notification=True, reply_markup=weather_items_btn
        )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
