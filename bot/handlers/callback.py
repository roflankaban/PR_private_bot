from pyexpat import model
from aiogram import Bot
from aiogram.client import bot
from aiogram.types import CallbackQuery
from token_api import CHAT_ID

    


async def verify23123(call: CallbackQuery,bot:Bot):
    answer = f"Ваше замовлення підтверджено. Невдовзі з вами зв’яжеться наш персонал"
    await bot.send_message(chat_id=CHAT_ID, text=data_order)