from Utils.SQL_actions import sql
# OUT Параметры процедцры в листе аргумента должен быть 0


def get_const(name_const: str) -> str:
    args_proc = [name_const, 0]
    value_const = sql.call_procedure_return_one_from_db('get_const_db', args_proc)
    return value_const


def find_user_bd(user_tg_id: str) -> bool:
    args_proc = [user_tg_id, 0]
    USER = sql.call_procedure_return_one_from_db('get_is_user_in_bd', args_proc)
    is_user_found = bool(int(USER))
    return is_user_found


def insert_user_in_db(user_id: int,
                      user_name: str,
                      user_login_tg: str) -> None:
    args_proc = [user_id, user_name, user_login_tg]
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
    id_survey = sql.call_procedure_return_one_from_db('set_survey_name_get_id_survey', args_proc)
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


if __name__ == '__main__':
    try:
        # set_survey(2, 2, 'Who I am? ______', 'I', 'You', 'Vadim', 'Volan de Mort', 1)
        VALUE = find_user_bd(5436880841)
        print(VALUE)
    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
