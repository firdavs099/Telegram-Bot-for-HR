from aiogram.dispatcher.filters.state import State, StatesGroup


class get_data(StatesGroup):
    name = State()
    db = State()
    phone = State()
    is_student = State()
    loc = State()
    shiftt = State()
    exp = State()
