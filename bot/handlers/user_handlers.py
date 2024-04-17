from aiogram.utils.markdown import hbold
from keyboards.reply import get_reply_keyboard
from aiogram import types

async def get_iluha(message: types.Message) -> None:
    await message.answer_photo(
        types.FSInputFile(path="bot/images/iluha.jpg"), caption="Цей чорт ніхуя не робить"
    )
    

async def get_furry(message: types.Message) -> None:
    await message.answer_photo(
        types.FSInputFile(path="bot/images/furry.jfif"), caption="https://t.me/AnitiHentai"
    )


async def get_start(message: types.Message) -> None:
    """Processes the `start` command"""
    reply_text = f'Привіт! {hbold(message.from_user.first_name)}. Я бот агенства FAVEX. З радістю допоможу вам з послугами, що вас цікавлять. Просто оберіть послугу, і ми розпочнемо роботу! 🤖💼'
    
    await message.answer(reply_text,
                     reply_markup=get_reply_keyboard())
