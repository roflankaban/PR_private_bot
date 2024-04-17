import logging
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify


async def get_services(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, почнемо формувати вимоги.\r\nТип вашої послуги ''(наприклад Створення дизайну квартир)''')
    await state.update_data(username=message.from_user.username)
    await state.set_state(StepsForm.GET_SERVICES)
    

async def get_services_type(message: Message, state: FSMContext):
    await message.answer(f'Ви надаєте послуги: {message.text}\r\nТепер введіть більш детальний опис ваших послуг (додайте посилання якщо воно є)')
    await state.update_data(services=message.text)
    await state.set_state(StepsForm.GET_SERVICES_TYPES)
    

async def get_details(message: Message, state: FSMContext):
    await message.answer(f'Ваш детальний опис: {message.text}\r\n')
    await state.update_data(services_type=message.text)
    context_data = await state.get_data()
    services = context_data.get('services')
    services_type = context_data.get('services_type')
    data_order = f'Підтвердіть вашу інформацію\r\n' \
                 f'@{hbold(message.from_user.username)}\r\n'\
                 f'Ви надаєте послуги: {services}\r\n' \
                 f'Ваша більш детальна інформація: {services_type}\r\n' 
    await message.answer(data_order, reply_markup=inline_verify)
    logging.info('Відбулося замовлення рекламу сервісу')
    await state.set_state(StepsForm.VERIFIED_SERVICES)
