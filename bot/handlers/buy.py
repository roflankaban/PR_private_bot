from aiogram.types import  Message, Update
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify
import logging


async def get_buy(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, почнемо формувати вимоги.\r\nВведіть ваш рекламний бюджет')
    await state.update_data(username=message.from_user.username)
    await state.set_state(StepsForm.GET_BUDGET)
    

async def get_budget(message: Message, state: FSMContext):
    await message.answer(f'Ваш бюджет: {message.text}\r\nТепер введіть посилання на ваш канал')
    await state.update_data(budget=message.text)
    await state.set_state(StepsForm.GET_LINK)
    

async def get_link(message: Message, state: FSMContext):
    await message.answer(f'Посилання на ваш канал: {message.text}\r\n')
    await state.update_data(link=message.text)
    context_data = await state.get_data()
    budget = context_data.get('budget')
    link = context_data.get('link')
    data_order = f'Підтвердіть вашу інформацію\r\n' \
                 f'@{hbold(message.from_user.username)}\r\n'\
                 f'Ваш рекламний бюджет: {budget}\r\n' \
                 f'Посилання на ваш канал: {link}\r\n' 
    await message.answer(data_order, reply_markup=inline_verify)
    logging.info('Відбулося замовлення закупки реклами')
    await state.set_state(StepsForm.VERIFIED_BUY)