from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup

state_storage = StateMemoryStorage()


class MyStates(StatesGroup):
    user_id = State()
    give = State()
    take = State()
    amount = State()
    get = State()
    get2 = State()
    get3 = State()
    phone = State()

