from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from token_api import CHAT_ID
from keyboards.reply import get_reply_keyboard
from bot_instance import bot

    


async def notverify(call: CallbackQuery, state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    await message.answer(f"Ваше замовлення видалено",reply_markup=get_reply_keyboard())
    context_data = await state.get_data()
    username = context_data.get('username')
    print('Canseled order by @',username)
    await call.answer()
    await state.clear()
    

#ЗАКУП РЕКЛАМИ
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
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    print('Oordered AD buy for @',username)
    await call.answer()
    await state.clear()
    


#ПРОСУВАННЯ ПОСЛУГ
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
    print('Service promo for @',username)
    await call.answer()
    await state.clear()
    
    
#КРЕО
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
    print('Ordered kreo for @',username)
    await call.answer()
    await state.clear()
    

#КАНАЛ ПІД КЛЮЧ
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
    print('Ordered creating tg channes for @',username)
    await call.answer()
    await state.clear()
    

async def verify_buy_course(call: CallbackQuery,state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    username = context_data.get('username')
    data_order = f'@{username}\r\n'\
                 f'КУРС ПО ЗАКУПУ\r\n'
    await message.answer(f"Очікуйте повідомлення від нашого персоналу",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    print('Ordered how to buy course @',username)
    await call.answer()
    

async def verify_kero_course(call: CallbackQuery,state: FSMContext):
    message = call.message  # Отримуємо повідомлення, пов'язане з цим запитом
    context_data = await state.get_data()
    username = context_data.get('username')
    data_order = f'@{username}\r\n'\
                 f'КУРС ПО КРЕО\r\n'
    await message.answer(f"Очікуйте повідомлення від нашого персоналу",reply_markup=get_reply_keyboard())
    await bot.send_message(chat_id=CHAT_ID, text=data_order)
    print('Ordered kreo course @',username)
    await call.answer()