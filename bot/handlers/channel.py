import logging
from aiogram.types import CallbackQuery, Message, Update
from aiogram.fsm.context import FSMContext
from token_api import CHAT_ID
from utils.statesform import StepsForm
from bot_instance import bot
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify
from keyboards.reply import get_reply_keyboard


async def get_channel(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, почнемо формувати вимоги.\r\nВведіть тематику вашого каналу')
    await state.update_data(username=message.from_user.username)
    await state.set_state(StepsForm.GET_THEMATIC)
    

async def get_thematic(message: Message, state: FSMContext):
    await message.answer(f'Ваша тематика: {message.text}\r\nТепер введіть який термін є тіпа за який час')
    await state.update_data(thematic=message.text)
    await state.set_state(StepsForm.GET_TIME)
    

async def get_time(message: Message, state: FSMContext):
    await message.answer(f'Термін є тіпа за який час: {message.text}\r\nТепер термін виконання')
    await state.update_data(time=message.text)
    context_data = await state.get_data()
    thematic = context_data.get('thematic')
    time = context_data.get('time')
    data_order = f'Підтвердіть вашу інформацію\r\n' \
                 f'@{hbold(message.from_user.username)}\r\n'\
                 f'Ваша тематика: {thematic}\r\n' \
                 f'Термін виконання: {time}\r\n' 
    await message.answer(data_order, reply_markup=inline_verify)
    logging.info('Відбулося замовлення канала під ключ')
    await state.set_state(StepsForm.VERIFIED_CHANNEL)
    

async def verify_channel(call: CallbackQuery, state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    username = context_data.get('username')
    thematic = context_data.get('thematic')
    time = context_data.get('time')
    data_order = f'@{username}\r\n'\
                 f'КАНАЛ ПІД КЛЮЧ\r\n'\
                 f'Ваша тематика: {thematic}\r\n' \
                 f'Термін виконання: {time}\r\n' 
    await message.answer(f"Ваше замовлення підтверджено. Невдовзі з вами зв’яжеться наш персонал",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    await state.clear()