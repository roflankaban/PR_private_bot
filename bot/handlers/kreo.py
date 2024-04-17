import logging
from keyboards.inline import inline_verify
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from aiogram.utils.markdown import hbold


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
    logging.info('Відбулося замовлення крео')
    await state.set_state(StepsForm.VERIFIED)
