import asyncio 
from aiogram import Dispatcher,F
from aiogram.filters import CommandStart, Command
from handlers.buy import get_budget, get_buy, get_link, verify_buy
from utils.statesform import StepsForm
from bot_instance import bot
from handlers.user_handlers import get_start
from handlers.kreo import get_audience, get_form, get_others, get_theme,get_post_type, verify
from handlers.buy import get_buy,get_budget,get_link,verify_buy
from handlers.channel import get_channel, get_thematic,get_time,verify_channel
from handlers.service import get_services,get_details,get_services_type, verify_services

async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    
    dp = Dispatcher()
    dp.message.register(get_start, F.text == "/start")
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

    
    dp.callback_query.register(verify,StepsForm.VERIFIED)
    dp.callback_query.register(verify_buy,StepsForm.VERIFIED_BUY)
    dp.callback_query.register(verify_channel,StepsForm.VERIFIED_CHANNEL)
    dp.callback_query.register(verify_services,StepsForm.VERIFIED_SERVICES)
    
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())