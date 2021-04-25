import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from views import take_data

API_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['Hi', 'hi', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)

@dp.message_handler()
async def weather_bot(message: types.Message):
    data = take_data(message.text)
    await message.answer(str(data))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
