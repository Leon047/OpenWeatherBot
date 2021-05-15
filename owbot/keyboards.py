from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

# ...
button_help = KeyboardButton('London')
hi_btn = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help)

# ...
button_main = KeyboardButton('/main')
button_clouds = KeyboardButton('/clouds')
button_sys = KeyboardButton('/sys')
button_coord = KeyboardButton('/coord')

# ...
button_weather_items = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button_main, button_clouds, button_sys, button_coord
)
