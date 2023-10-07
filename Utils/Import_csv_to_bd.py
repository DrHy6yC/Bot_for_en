from pathlib import Path

from Create_bot import sql
from Utils import SQL_querys as querys
from Read_file import import_csv


def import_survey_csv(path_file: str, description_test: str) -> None:
    path = Path(__file__).parent / f"../{path_file}"
    csv_file = import_csv(path)
    name_test = path_file.replace('.csv', '')

    sql.insert_update_db(
        query=querys.insert_SURVEYS_by_SURVEY_NAME_and_SURVEY_DESCRIPTION,
        data={'SURVEY_NAME': name_test, 'SURVEY_DESCRIPTION': description_test}
    )
    id_survey = sql.select_db_one(
        query=querys.select_SURVEY_ID_from_SURVEY_by_SURVEY_NAME,
        data={'SURVEY_NAME': name_test}
    )

    for i in csv_file:
        num_question = i['NumberQuestion']
        question = i['Question']
        answer_1 = i['Answer1']
        answer_2 = i['Answer2']
        answer_3 = i['Answer3']
        answer_4 = i['Answer4']
        true_answer = i['TrueAnswer']
        sql.insert_update_db(
            query=querys.insert_SURVEYS_QUESTIONS_by_SURVEY_ID_and_NUMBER_QUESTION_and_SURVEY_QUESTION,
            data={'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'SURVEY_QUESTION': question}
        )
        sql.insert_update_db(
            query=querys.insert_SURVEYS_TRUE_ANSWERS_by_SURVEY_ID_and_NUMBER_QUESTION_and_NUMBER_TRUE_ANSWER,
            data={'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'NUMBER_TRUE_ANSWER': true_answer}
        )
        print('NUMBER_ANSWER:', 1, 'SURVEY_ID:', id_survey, 'NUMBER_QUESTION:', num_question, 'SURVEY_ANSWER:', answer_1)
        sql.insert_update_db(
            query=querys.insert_SURVEYS_ANSWERS_by_NUMBER_ANSWER_and_SURVEY_ID_and_NUMBER_QUESTION_and_SURVEY_ANSWER,
            data={'NUMBER_ANSWER': 1, 'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'SURVEY_ANSWER': answer_1}
        )
        sql.insert_update_db(
            query=querys.insert_SURVEYS_ANSWERS_by_NUMBER_ANSWER_and_SURVEY_ID_and_NUMBER_QUESTION_and_SURVEY_ANSWER,
            data={'NUMBER_ANSWER': 2, 'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'SURVEY_ANSWER': answer_2}
        )
        sql.insert_update_db(
            query=querys.insert_SURVEYS_ANSWERS_by_NUMBER_ANSWER_and_SURVEY_ID_and_NUMBER_QUESTION_and_SURVEY_ANSWER,
            data={'NUMBER_ANSWER': 3, 'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'SURVEY_ANSWER': answer_3}
        )
        sql.insert_update_db(
            query=querys.insert_SURVEYS_ANSWERS_by_NUMBER_ANSWER_and_SURVEY_ID_and_NUMBER_QUESTION_and_SURVEY_ANSWER,
            data={'NUMBER_ANSWER': 4, 'SURVEY_ID': id_survey, 'NUMBER_QUESTION': num_question, 'SURVEY_ANSWER': answer_4}
        )


if __name__ == '__main__':
    import_survey_csv('miniTest.csv', 'Маленький проверочный тест для проверки всего')
