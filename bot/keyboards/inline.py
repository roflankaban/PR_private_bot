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
            text='FAVEX',
            url='https://t.me/+R084uaIG0BIxZTc6'
        )
    ]
])

study_markup = InlineKeyboardMarkup(inline_keyboard=[
    [
            InlineKeyboardButton(
            text='Курс з розробки креативів',
            callback_data='creative_course',
        ),
        InlineKeyboardButton(
            text='Курс з закупу',
            callback_data='buy_course',
        )
    ]
    ])
