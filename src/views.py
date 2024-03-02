"""
views.py - Module for defining view functions and handling user
interactions in the project.
"""
from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction

from .messages import help_msg, start_msg
from .models import OpenWeather
from .keyboards import mk_help_buttons, mk_main_buttons

# All handlers should be attached to the Router.
router = Router(name=__name__)

# An instance of the class for OpenWeather api.
api = OpenWeather()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply_photo(
        photo = types.FSInputFile(
            path = './static/img/logo.png',
            filename = 'logo.png'
        ),
        caption = start_msg
    )

@router.message(F.text=='help')
async def send_help(message: types.Message):
    """Help request handler"""
    await message.answer(
        text = help_msg,
        reply_markup=mk_help_buttons()
    )

@router.message(F.text=='main')
async def send_main(message: types.Message):
    """Main button handler"""
    await message.reply(api.weather_item('main'))

@router.message(F.text=='clouds')
async def send_clouds(message: types.Message):
    """Clouds button handler"""
    await message.reply(api.weather_item('clouds'))

@router.message(F.text=='sys')
async def send_sys(message: types.Message):
    """Sys button handler"""
    await message.reply(api.weather_item('sys'))

@router.message(F.text=='coord')
async def send_coord(message: types.Message):
    """Coord button handler"""
    await message.reply(api.weather_item('coord'))

@router.message()
async def open_weather_main(message: types.Message):
    """Main request handler
    It takes the name of a country or city and returns a weather forecast.
    """
    # await message.bot.send_chat_action(
    #     chat_id = message.chat.id,
    #     action = ChatAction.UPLOAD_PHOTO
    # )

    response = api.main_request(message.text)

    if 'error_msg' in response.keys():

        error_icon = response['error_icon']
        error_msg = response['error_msg']

        await message.reply_photo(
            photo = types.FSInputFile(
                path = f'./static/img/{error_icon}',
                filename = error_icon,
            ),
            caption = error_msg,
            reply_markup = mk_help_buttons(),
        )
    else:
        icon = response['icon']
        main = response['main']

        await message.reply_photo(
            photo = types.FSInputFile(
                path = f'./static/img/{icon}',
                filename = icon,
            ),
            caption = main,
            disable_notification = True,
            reply_markup = mk_main_buttons(),
        )
