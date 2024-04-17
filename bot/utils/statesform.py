from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_AUDIENCE = State()
    GET_THEME = State()
    GET_POST_TYPE = State()
    GET_OTHERS = State()
    VERIFIED = State()

    GET_BUDGET = State()
    GET_LINK = State()
    VERIFIED_BUY = State()

    GET_TIME = State()
    GET_THEMATIC = State()
    VERIFIED_CHANNEL = State()
    
    GET_SERVICES = State()
    GET_SERVICES_TYPES = State()
    VERIFIED_SERVICES = State()