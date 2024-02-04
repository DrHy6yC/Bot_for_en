from icecream import ic
from Utils.SQL_actions import sql


# OUT Параметры процедцры в листе аргумента должен быть 0


def get_const(name_const: str) -> str:
    args_proc = [name_const, 0]
    value_const = sql.call_procedure_return_one_from_db('get_const_db', args_proc)
    return value_const


def find_user_bd(user_tg_id: int) -> bool:
    args_proc = [user_tg_id, 0]
    USER = sql.call_procedure_return_one_from_db('get_is_user_in_bd', args_proc)
    is_user_found = bool(int(USER))
    return is_user_found


def insert_user_in_db(user_id: int,
                      user_name: str,
                      user_login_tg: str,
                      message_id: int) -> None:
    args_proc = [user_id, user_name, user_login_tg, message_id]
    sql.call_procedure_changed_db('set_user_in_bd', args_proc)


def get_id_survey(name_survey: str) -> int:
    args_proc = [name_survey, 0]
    id_survey = int(sql.call_procedure_return_one_from_db('get_id_survey_db', args_proc))
    return id_survey


def get_answer(test_id: int,
               num_question: int) -> list:
    args_proc = [test_id, num_question]
    answer_list = sql.call_procedure_return_table('get_answer', args_proc)
    return answer_list


def get_question(num_question: int,
                 id_survey: int) -> str:
    args_proc = [num_question, id_survey, 0]
    question_txt = sql.call_procedure_return_one_from_db('get_question', args_proc)
    return question_txt


def get_question_by_id_question(id_question: int) -> str:
    args_proc = [id_question, 0]
    question_txt = sql.call_procedure_return_one_from_db('get_question_by_id_question', args_proc)
    return question_txt


def get_one_answer(num_question: int,
                   id_survey: int,
                   num_answer: int) -> str:
    args_proc = [num_question, id_survey, num_answer, 0]
    answer_txt = sql.call_procedure_return_one_from_db('get_one_answer', args_proc)
    return answer_txt


def get_name_survey() -> list:
    args_proc = []
    answer_list = sql.call_procedure_return_table('get_name_survey', args_proc)
    return answer_list


def set_survey_name_get_id_survey(name_survey: str,
                                  description_survey: str) -> int:
    args_proc = [name_survey, description_survey, 0]
    id_survey = sql.call_procedure_return_changed_one('set_survey_name_get_id_survey', args_proc)
    return id_survey


def set_survey(id_survey: int,
               num_question: int,
               question: str,
               answer_1: str,
               answer_2: str,
               answer_3: str,
               answer_4: str,
               true_answer: int) -> None:
    args_proc = [id_survey,
                 num_question,
                 question,
                 answer_1,
                 answer_2,
                 answer_3,
                 answer_4,
                 true_answer]
    answer_list = sql.call_procedure_return_changed_one('set_survey', args_proc)
    return answer_list


def get_is_name_survey(name_test: str) -> bool:
    args_proc = [name_test, 0]
    is_name = sql.call_procedure_return_one_from_db('get_is_name_survey', args_proc)
    return bool(is_name)


def get_count_question(id_test: int) -> int:
    args_proc = [id_test, 0]
    count_question = sql.call_procedure_return_one_from_db('get_count_question', args_proc)
    return int(count_question)


def set_user_survey_get_id_user_survey(user_id: int, id_test: int, status_test: int) -> int:
    args_proc = [user_id, id_test, status_test, 0]
    id_user_survey = sql.call_procedure_return_changed_one('set_user_survey_get_id_user_survey', args_proc)
    return int(id_user_survey)


def get_is_user_status_survey(user_id: int, status: int) -> bool:
    args_proc = [user_id, status, 0]
    is_user_status_survey = int(sql.call_procedure_return_one_from_db('get_is_user_status_survey', args_proc))
    return bool(is_user_status_survey)


def get_user_survey(user_id: int, status: int) -> list:
    args_proc = [user_id, status]
    user_survey_list = sql.call_procedure_return_table('get_user_survey', args_proc)
    if user_survey_list:
        return user_survey_list
    else:
        return list()


def get_user_survey_by_user_survey_id(user_survey_id: int) -> list:
    args_proc = [user_survey_id]
    user_survey_list = sql.call_procedure_return_table('get_user_survey_by_user_survey_id', args_proc)
    if user_survey_list:
        return user_survey_list[0]
    else:
        return list()


def set_question_num(question_num: int, user_test_id: int) -> None:
    args_proc = [question_num, user_test_id]
    sql.call_procedure_changed_db('set_question_num', args_proc)


def set_user_survey_status_test(user_test_id: int, status: int) -> None:
    args_proc = [user_test_id, status]
    sql.call_procedure_changed_db('set_user_survey_status_test', args_proc)


def set_user_answer(id_answer: int, user_survey_id: int, num_question: int) -> None:
    args_proc = [id_answer, user_survey_id, num_question]
    sql.call_procedure_changed_db('set_user_answer', args_proc)


def get_answer_id(id_test: int, num_question: int, num_answer: int) -> int:
    args_proc = [id_test, num_question, num_answer, 0]
    answer_id = sql.call_procedure_return_one_from_db('get_answer_id', args_proc)
    return int(answer_id)


def comparison_answer(id_user_test: int) -> int:
    ic.disable()
    balls = 0
    args_proc = [id_user_test]
    answer_user = dict(sql.call_procedure_return_table('get_answer_user_by_id_user_test', args_proc))
    answer_true = dict(sql.call_procedure_return_table('get_answer_true_by_id_user_test', args_proc))
    ic(answer_user, answer_true)
    for num, answer in answer_true.items():
        ic(num, answer, answer_user.get(num, 0))
        if answer_true[num] == answer_user.get(num, 0):
            balls += 1
    ic.enable()
    return balls


def set_balls(id_user_test: int, balls: int) -> None:
    args_proc = [id_user_test, balls]
    sql.call_procedure_changed_db('set_balls', args_proc)


def get_balls(id_user_test: int) -> int:
    args_proc = [id_user_test, 0]
    ball = sql.call_procedure_return_one_from_db('get_balls', args_proc)
    return int(ball)


def get_end_result_test(id_user: int) -> int:
    args_proc = [id_user, 0]
    ball = sql.call_procedure_return_one_from_db('get_end_result_test', args_proc)
    return int(ball)


if __name__ == '__main__':
    try:
        # set_balls(95, 1)
        VALUE = get_end_result_test(809916411)
        ic(VALUE)
    except Exception as error_exception:
        ic('Error main file')
        ic(error_exception)
    finally:
        sql.end_con()
