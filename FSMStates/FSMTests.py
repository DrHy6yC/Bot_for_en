from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMTest(StatesGroup):
    test_handler = State()
    test_run = State()
    test_progressed = State()
    test_completed = State()
    test_revoked = State()
