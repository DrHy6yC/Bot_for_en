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


# select_test = CallbackData('select_test', 'name_test')
del_message = DelMessageCal()
# cancel_test = CallbackData('cancel', 'id_user_test')
# run_test = CallbackData('run_test', 'name_test')
# start_test = CallbackData('start_test', 'id_answer')
# continue_test = CallbackData('continue_test', 'id_user_test')
# restart_test = CallbackData('restart_test', 'id_user_test')
# view_result = CallbackData('view_result', 'id_user_test')
# stop_test = CallbackData('stop_result', 'id_user_test')
