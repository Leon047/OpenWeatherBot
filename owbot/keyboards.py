from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# ...
washington = KeyboardButton('Washington')
london = KeyboardButton('London')
kiev = KeyboardButton('Kyiv')

# ...
help_btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    washington, london, kiev
).add(KeyboardButton('My location 🗺️', request_location=True)
)

# ...
button_main = KeyboardButton('/main')
button_clouds = KeyboardButton('/clouds')
button_sys = KeyboardButton('/sys')
button_coord = KeyboardButton('/coord')

# ...
weather_items_btn = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button_main, button_clouds, button_sys, button_coord
)
