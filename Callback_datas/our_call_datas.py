from aiogram.filters.callback_data import CallbackData


class DelMessageCal(CallbackData, prefix='del_message'):
    pass


class SelectTestCal(CallbackData, prefix='select_test'):
    name_test: str


class ProgressTestCal(CallbackData, prefix='progress_test'):
    id_answer: str


class CanceledTestCal(CallbackData, prefix='canceled_test'):
    id_user_test: int


class ViewResultTestCal(CallbackData, prefix='view_result_test'):
    id_user_test: int


class StopTestCal(CallbackData, prefix='stop_test'):
    id_user_test: int


class RestartTestCal(CallbackData, prefix='restart_test'):
    id_user_test: int


class ContinueTestCal(CallbackData, prefix='continue_test'):
    id_user_test: int


del_message = DelMessageCal()
