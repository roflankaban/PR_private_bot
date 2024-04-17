from aiogram.types import CallbackQuery, Message, Update
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from bot_instance import bot
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify
from keyboards.reply import get_reply_keyboard
from token_api import CHAT_ID


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
    await state.set_state(StepsForm.VERIFIED_SERVICES)
    

async def verify_services(call: CallbackQuery, state: FSMContext,):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    username = context_data.get('username')
    services = context_data.get('services')
    services_type = context_data.get('services_type')
    data_order = f'ПРОСУВАННЯ ПОСЛУГ\r\n' \
                 f'@{username}\r\n'\
                 f'Ви надаєте послуги: {services}\r\n' \
                 f'Ваша більш детальна інформація: {services_type}\r\n' 
    await message.answer(f"Ваше замовлення підтверджено. Невдовзі з вами зв’яжеться наш персонал",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    await state.clear()