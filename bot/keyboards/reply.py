from ctypes import resize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    
    keyboard_builder.button(text='Рекламний креатив')
    keyboard_builder.button(text='Закуп під ваш телеграм канал')
    keyboard_builder.button(text='Телеграм канал під ключ')
    keyboard_builder.button(text='Просування ваших послуг')
    keyboard_builder.adjust(1,1,1,1)
    return keyboard_builder.as_markup(resize_keyboard=True,
                                      one_time_keyboard=True,
                                      input_field_placeholder="Обери функцію"
                                      )