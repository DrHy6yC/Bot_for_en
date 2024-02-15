from aiogram.utils.callback_data import CallbackData

select_test = CallbackData('select_test', 'name_test')
del_message = CallbackData('del_message')
cancel = CallbackData('cancel', 'type_cancel', 'id_user_test')
run_test = CallbackData('run_test', 'name_test')
start_test = CallbackData('start_test', 'id_answer')
continue_test = CallbackData('continue_test', 'id_user_test')
restart_test = CallbackData('restart_test', 'id_user_test')
view_result = CallbackData('view_result', 'id_user_test')
