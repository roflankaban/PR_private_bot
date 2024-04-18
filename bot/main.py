import asyncio
from tabnanny import check 
from aiogram import Dispatcher,F
from utils.statesform import StepsForm
from bot_instance import bot
from handlers.user_handlers import get_start,get_iluha,get_furry
from handlers.kreo import get_audience, get_form, get_others, get_theme,get_post_type
from handlers.buy import get_buy,get_budget,get_link
from handlers.channel import get_channel, get_thematic,get_time
from handlers.service import get_services,get_details,get_services_type
from handlers.callback import verify_buy,verify_services,verify,verify_channel,notverify

import os

current_directory = os.getcwd()
print("Поточна директорія:", current_directory)

async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    
    
    dp = Dispatcher()
    dp.message.register(get_start, F.text == "/start")
    dp.message.register(get_iluha, F.text == "/iluha")
    dp.message.register(get_furry, F.text == "/furry")
    dp.message.register(get_form,F.text == 'Рекламний креатив' )
    dp.message.register(get_buy,F.text == 'Закуп під ваш телеграм канал')
    dp.message.register(get_channel,F.text == 'Телеграм канал під ключ')
    dp.message.register(get_services,F.text == 'Просування ваших послуг')
    
    dp.message.register(get_audience,StepsForm.GET_AUDIENCE)
    dp.message.register(get_theme,StepsForm.GET_THEME)
    dp.message.register(get_post_type,StepsForm.GET_POST_TYPE)
    dp.message.register(get_others,StepsForm.GET_OTHERS)
    
    dp.message.register(get_budget,StepsForm.GET_BUDGET)
    dp.message.register(get_link,StepsForm.GET_LINK)


    dp.message.register(get_thematic,StepsForm.GET_THEMATIC)
    dp.message.register(get_time,StepsForm.GET_TIME)


    dp.message.register(get_services_type,StepsForm.GET_SERVICES)
    dp.message.register(get_details,StepsForm.GET_SERVICES_TYPES)

    
    dp.callback_query.register(verify,F.data.startswith('1'),StepsForm.VERIFIED)
    dp.callback_query.register(verify_buy,F.data.startswith('1'),StepsForm.VERIFIED_BUY)
    dp.callback_query.register(verify_channel,F.data.startswith('1'),StepsForm.VERIFIED_CHANNEL)
    dp.callback_query.register(verify_services,F.data.startswith('1'),StepsForm.VERIFIED_SERVICES)
    dp.callback_query.register(notverify,F.data.startswith('2'))
    
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())