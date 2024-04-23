from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from token_api import SUB_ID
from keyboards.inline import startup_markup
from keyboards.reply import get_reply_keyboard
from keyboards.inline import study_markup
from aiogram import types
from bot_instance import bot

async def get_iluha(message: Message) -> None:
    await message.answer_photo(
        types.FSInputFile(path="bot/images/iluha.jpg"), caption="Цей чорт ніхуя не робить"
    )
    

async def get_furry(message: Message) -> None:
    await message.answer_photo(
        types.FSInputFile(path="bot/images/furry.jfif"), caption="https://t.me/AnitiHentai"
    )


async def get_study(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.from_user.username)
    await message.answer('Оберіть що вас цікавить і з вами звяжеться наш менеджер для більш детальної інформації',reply_markup=study_markup)



async def check_subscription(user_id: int, channel_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in ['creator', 'administrator', 'member']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False
 
async def get_start(message: Message):
    user_id = message.from_user.id
    
    if await check_subscription(user_id, SUB_ID):
        reply_text = f'Вітаю {hbold(message.from_user.first_name)}.\r\n' \
                     f'Мене звати Креобот, я бот від компанії FAVEX. \r\n' \
                     f'Я створений для того щоб покращити зручність та якість вашої рекламної кампанії. \r\n' \
                     f'Для початку потрібно обрати послугу яка вас цікавить. \r\n'
        await message.answer(reply_text,
                     reply_markup=get_reply_keyboard())
    else:
        await message.reply("Ви не підписані на канал. Будь ласка підпишіться на канал щоб використовувати бота.",reply_markup=startup_markup)