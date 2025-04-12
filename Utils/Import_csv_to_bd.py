from pathlib import Path

from icecream import ic

from Create_bot import bot
from Utils.Read_file import import_csv
from SQL import ORM
from SQL.Models import QuizzesORM, QuizeQuestionsORM, QuizeAnswersORM, QuizeTrueAnswersORM


def get_id_answer(answers: list[QuizeAnswersORM], num_true_answer: int) -> int:
    for answer in answers:
        if num_true_answer == answer.ANSWER_NUMBER:
            return answer.ID


async def async_import_survey_csv(path_file: str, description_test: str) -> None:
    """
    Notes:
        Ищет файл в корне проекта, можно вводить просто имя и расширение файла ("Name_file.csv")

    Parameters
    ----------
    path_file
    description_test

    Returns
    -------

    """
    path = Path(__file__).parent.parent/f"CSV_Files/{path_file}"
    csv_file = import_csv(str(path))
    name_test = path_file.replace('.csv', '')

    if await ORM.async_is_test_in_bd(name_test):
        await bot.send_message(chat_id=809916411,
                               text='Тест с таким именем уже есть')
        ic("Тест с таким именем уже есть")
    else:
        test = QuizzesORM(
            QUIZE_NAME=name_test,
            QUIZE_DESCRIPTION=description_test
        )
        await ORM.async_insert_data_list_to_bd(
            [test]
        )
        test = await ORM.async_get_test_by_name(name_test)
        for i in csv_file:
            num_question = int(i['NumberQuestion'])
            question = QuizeQuestionsORM(
                ID_QUIZE=test.ID,
                QUESTION_NUMBER=num_question,
                QUESTION_TEXT=i['Question']
            )
            answer_1 = QuizeAnswersORM(
                ID_QUIZE=test.ID,
                QUESTION_NUMBER=num_question,
                ANSWER_NUMBER=1,
                ANSWER_TEXT=i['Answer1']
            )
            answer_2 = QuizeAnswersORM(
                ID_QUIZE=test.ID,
                QUESTION_NUMBER=num_question,
                ANSWER_NUMBER=2,
                ANSWER_TEXT=i['Answer2']
            )
            answer_3 = QuizeAnswersORM(
                ID_QUIZE=test.ID,
                QUESTION_NUMBER=num_question,
                ANSWER_NUMBER=3,
                ANSWER_TEXT=i['Answer3']
            )
            answer_4 = QuizeAnswersORM(
                ID_QUIZE=test.ID,
                QUESTION_NUMBER=num_question,
                ANSWER_NUMBER=4,
                ANSWER_TEXT=i['Answer4']
            )
            await ORM.async_insert_data_list_to_bd(
                [question, answer_1, answer_2, answer_3, answer_4]
            )
            answers = await ORM.async_get_answers_by_id_test_and_num_question(
                test.ID, num_question
            )

            num_answer = int(i['TrueAnswer'])
            id_answer = get_id_answer(answers, num_answer)
            true_answer = QuizeTrueAnswersORM(
                ID_QUIZE=test.ID,
                ID_ANSWER=id_answer,
                QUESTION_NUMBER=num_question,
            )
            await ORM.async_insert_data_list_to_bd(
                [true_answer]
            )
