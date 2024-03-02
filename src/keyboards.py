"""
keyboards.py - Module for creating custom keyboards in the project.
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Mk help buttons.
def mk_help_buttons() -> ReplyKeyboardMarkup:
    washington = KeyboardButton(text='Washington')
    london = KeyboardButton(text='London')
    kyiv = KeyboardButton(text='Kyiv')

    help_btn_row = [washington, london, kyiv]

    return ReplyKeyboardMarkup(keyboard=[help_btn_row], resize_keyboard=True)

# Mk main buttons.
def mk_main_buttons() -> ReplyKeyboardMarkup:
    btn_main = KeyboardButton(text='main')
    btn_clouds = KeyboardButton(text='clouds')
    btn_sys = KeyboardButton(text='sys')
    btn_coord = KeyboardButton(text='coord')

    main_btn_row = [btn_main, btn_clouds, btn_sys, btn_coord]

    return ReplyKeyboardMarkup(keyboard=[main_btn_row], resize_keyboard=True)
