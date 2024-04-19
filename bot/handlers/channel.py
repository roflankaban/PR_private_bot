import logging
from aiogram.types import Message, Update
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify


async def get_channel(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, почнемо формувати вимоги.\r\nВведіть тематику вашого каналу')
    await state.update_data(username=message.from_user.username)
    await state.set_state(StepsForm.GET_THEMATIC)
    

async def get_thematic(message: Message, state: FSMContext):
    await message.answer(f'Ваша тематика: {message.text}\r\nТепер введіть який термін виконання замовлення')
    await state.update_data(thematic=message.text)
    await state.set_state(StepsForm.GET_TIME)
    

async def get_time(message: Message, state: FSMContext):
    await message.answer(f'Термін виконанна замовлення: {message.text}\r\nТепер термін виконання')
    await state.update_data(time=message.text)
    context_data = await state.get_data()
    thematic = context_data.get('thematic')
    time = context_data.get('time')
    data_order = f'Підтвердіть вашу інформацію\r\n' \
                 f'@{hbold(message.from_user.username)}\r\n'\
                 f'Ваша тематика: {thematic}\r\n' \
                 f'Термін виконання: {time}\r\n' 
    await message.answer(data_order, reply_markup=inline_verify)
    await state.set_state(StepsForm.VERIFIED_CHANNEL)
