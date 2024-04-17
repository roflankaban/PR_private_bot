from aiogram.types import CallbackQuery, Message, Update
from aiogram.fsm.context import FSMContext
from utils.statesform import StepsForm
from bot_instance import bot
from aiogram.utils.markdown import hbold
from keyboards.inline import inline_verify
from keyboards.reply import get_reply_keyboard


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
    await state.set_state(StepsForm.VERIFIED_BUY)
    await  edit_message_reply_markup(chat_id=message.chat.id, reply_markup=None)
    

async def verify_buy(call: CallbackQuery, state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    username = context_data.get('username')
    budget = context_data.get('budget')
    link = context_data.get('link')
    data_order = f'@{username}\r\n'\
                 f'ЗАКУП РЕКЛАМИ\r\n'\
                 f'Ваш рекламний бюджет: {budget}\r\n' \
                 f'Посилання на ваш канал: {link}\r\n' 
    await message.answer(f"Ваше замовлення підтверджено. Невдовзі з вами зв’яжеться наш персонал",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=-1002054762566, text=data_order)
    await state.clear()