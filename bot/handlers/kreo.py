from keyboards.inline import inline_verify
from token_api import CHAT_ID
from aiogram.types import CallbackQuery
from aiogram.types import Message, Update
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from aiogram.utils.markdown import hbold
from bot_instance import bot
from keyboards.reply import get_reply_keyboard


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, почнемо формувати вимоги.\r\nВведіть вашу Цільову аудиторію')
    await state.update_data(username=message.from_user.username)
    await state.set_state(StepsForm.GET_AUDIENCE)

    

async def get_audience(message: Message,state: FSMContext):
    await message.answer(f'Твоя ЦА: {message.text}\r\nТепер введи тематику')
    await state.update_data(audience=message.text)
    await state.set_state(StepsForm.GET_THEME)
    

async def get_theme(message: Message,state: FSMContext):
    await message.answer(f'Твоя тематика: {message.text}\r\nТепер введи тип поста(прямий, байтовий, і тд)')
    await state.update_data(theme=message.text)
    await state.set_state(StepsForm.GET_POST_TYPE)
    

async def get_post_type(message: Message,state: FSMContext):
    await message.answer(f'Тип твого посту : {message.text}\r\nТепер введи інші побажання')
    await state.update_data(post_type=message.text)
    await state.set_state(StepsForm.GET_OTHERS)


async def get_others(message: Message, state: FSMContext):
    await message.answer(f'Твої інші побажання: {message.text}\r\n')
    await state.update_data(others=message.text)
    

    context_data = await state.get_data()
    audience = context_data.get('audience')
    theme = context_data.get('theme')
    post_type = context_data.get('post_type')
    others = context_data.get('others')
    data_order = f'Підтвердіть вашу інформацію\r\n' \
                 f'@{hbold(message.from_user.username)}\r\n'\
                 f'ЦА: {audience}\r\n' \
                 f'Тематика: {theme}\r\n' \
                 f'Пост: {post_type}\r\n' \
                 f'Інше: {others}\r\n'
    await message.answer(data_order, reply_markup=inline_verify)
    await state.set_state(StepsForm.VERIFIED)
    await bot.edit_message_reply_markup()
    
   
    

async def verify(call: CallbackQuery, state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    audience = context_data.get('audience')
    theme = context_data.get('theme')
    post_type = context_data.get('post_type')
    others = context_data.get('others')
    username = context_data.get('username')
    data_order = f'@{username}\r\n'\
                 f'КРЕО\r\n'\
                 f'ЦА: {audience}\r\n' \
                 f'Тематика: {theme}\r\n' \
                 f'Пост: {post_type}\r\n' \
                 f'Інше: {others}\r\n'
    await message.answer(f"Ваше замовлення підтверджено. Невдовзі з вами зв’яжеться наш персонал",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    await   state.clear()