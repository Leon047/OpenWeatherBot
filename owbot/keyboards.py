from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

# Help request buttons.
washington = KeyboardButton('Washington')
london = KeyboardButton('London')
kiev = KeyboardButton('Kyiv')

# Displays buttons in a help request handler.
help_btn = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(washington, london, kiev)

# Main request buttons.
button_main = KeyboardButton('/main')
button_clouds = KeyboardButton('/clouds')
button_sys = KeyboardButton('/sys')
button_coord = KeyboardButton('/coord')

# Display in a weather_main request handler.
weather_items_btn = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button_main, button_clouds, button_sys, button_coord
)
