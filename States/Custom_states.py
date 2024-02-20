from aiogram.fsm.state import StatesGroup, State

from SQL.Models import UserQuizzesORM


class TestStates(StatesGroup):
    select = State()
    run_test: UserQuizzesORM
    # progress = State()
    # canceled = State()
    # view_result = State()
    # continued = State()
    # stop = State()
    # restart = State()
