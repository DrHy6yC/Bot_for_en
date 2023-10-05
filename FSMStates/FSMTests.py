from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.fsm.state import StatesGroup, State


class FSMTest(StatesGroup):
    test_handler = State()
    test_run = State()
    test_progressed = State()
    test_continue = State()
    test_completed = State()
    test_revoked = State()
