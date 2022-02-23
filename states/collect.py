from aiogram.dispatcher.filters.state import State, StatesGroup


class Coll(StatesGroup):
    name = State()
    db = State()
    is_student = State()
    # shft = State()
    dist = State()
    exp = State()
