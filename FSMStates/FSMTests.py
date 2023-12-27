from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMTest(StatesGroup):
    no_test = State()
    test_handler = State()
    test_progressed = State()
    test_continue = State()
    test_completed = State()
    test_revoked = State()
