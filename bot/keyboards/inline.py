from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_verify = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Підтвердити',
            callback_data='1',
        ),
        InlineKeyboardButton(
            text='Відмінити',
            callback_data='2',
        )
    ]
])

startup_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Favex I Media Group',
            url='https://t.me/+0XxzoWMGnMZiNGQy',
        ),
        InlineKeyboardButton(
            text='Перевірити',
            callback_data='check',
        )
    ]
])
