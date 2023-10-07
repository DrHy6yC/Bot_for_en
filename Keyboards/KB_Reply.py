from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from Create_bot import sql
from Utils import SQL_querys as query


def set_but_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text="Помощь")
    b2 = KeyboardButton(text="Пройти тест")
    b3 = KeyboardButton(text="START")
    kb.add(b3, b1, b2)
    return kb


def set_IKB_one_but(text, call_data) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib = InlineKeyboardButton(text=text,
                              callback_data=call_data)
    ikb.add(ib)
    return ikb


def set_IKB_Survey(answers: list) -> InlineKeyboardMarkup:
    dictionary = dict()
    list_answers = answers
    i = 1
    for answer in list_answers:
        dictionary[answer] = str(i)
        i += 1
    dictionary['Остановить тест'] = '-1'
    ikb = set_IKB_many_but(dictionary)
    return ikb


def set_IKB_select_survey() -> InlineKeyboardMarkup:
    dictionary = dict()
    list_surveys = sql.select_db(query=query.select_SURVEY_NAME_from_SURVEY, data=dict())
    for name_test_list in list_surveys:
        name_test = name_test_list[0]
        dictionary[name_test] = f'Run test: {name_test}'

    ikb = set_IKB_many_but(dictionary)
    return ikb


def set_IKB_many_but(dictionary: dict) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for text, call in dictionary.items():
        ikb.add(InlineKeyboardButton(text=text,
                                     callback_data=call))
    return ikb


# TODO добавить клавиатуру для продолжения, перезапуска или окончательной отмены теста
def set_IKB_continue_finish() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text=f'Остановить тест',
                               callback_data='-1')
    ib2 = InlineKeyboardButton(text=f'Продолжить тест',
                               callback_data='0')
    ikb.add(ib1, ib2)
    return ikb