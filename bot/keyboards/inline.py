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
