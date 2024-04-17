from aiogram.filters import Command
from aiogram import Router, types
from aiogram.utils.markdown import hbold
from keyboards.reply import get_reply_keyboard


async def get_start(msg: types.Message) -> None:
    """Processes the `start` command"""
    reply_text = f'Доброго дня пане, {hbold(msg.from_user.first_name)}'
    
    await msg.answer(reply_text,
                     reply_markup=get_reply_keyboard())
    

#async def verify() -> None: