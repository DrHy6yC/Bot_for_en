from pathlib import Path

from Read_file import import_csv
from Utils.From_DB import set_survey_name_get_id_survey, set_survey


def import_survey_csv(path_file: str, description_test: str) -> None:
    path = Path(__file__).parent / f"../{path_file}"
    csv_file = import_csv(path)
    name_test = path_file.replace('.csv', '')
    # TODO Сделать проверку на то есть ли в бд такое имя теста

    id_survey = set_survey_name_get_id_survey(name_test, description_test)

    for i in csv_file:
        num_question = i['NumberQuestion']
        question = i['Question']
        answer_1 = i['Answer1']
        answer_2 = i['Answer2']
        answer_3 = i['Answer3']
        answer_4 = i['Answer4']
        true_answer = i['TrueAnswer']
        set_survey(id_survey, num_question, question, answer_1, answer_2, answer_3, answer_4, true_answer)


if __name__ == '__main__':
    import_survey_csv('English Level test. Grammar.csv', 'Проверка грамматики')
