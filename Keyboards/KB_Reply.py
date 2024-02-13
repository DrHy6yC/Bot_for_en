from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from SQL.models import QuizeAnswersORM
from Callback_datas import call_data_test


def set_but_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Помощь')
    b2 = KeyboardButton(text='Пройти тест')
    b3 = KeyboardButton(text='Узнать уровень')
    kb.add(b3, b1, b2)
    return kb


def set_IKB_one_but(text: str, call_data: CallbackData) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib = InlineKeyboardButton(text=text,
                              callback_data=call_data)
    ikb.add(ib)
    return ikb


def set_IKB_many_but(dictionary: dict[str, CallbackData]) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for text, call in dictionary.items():
        ikb.add(InlineKeyboardButton(text=text,
                                     callback_data=call))
    return ikb


def set_IKB_Survey(answers: list[QuizeAnswersORM]) -> InlineKeyboardMarkup:
    # TODO Переделать с использованием своей CallbackData
    dictionary = dict()
    list_answers = answers
    i = 1
    for answer in list_answers:
        dictionary[answer] = str(i)
        i += 1
    dictionary['Остановить тест'] = '-1'
    ikb = set_IKB_many_but(dictionary)
    return ikb


# def set_IKB_select_survey(dictionary) -> InlineKeyboardMarkup:
#     ikb = set_IKB_many_but(dictionary)
#     return ikb


def set_IKB_select_survey(names_tests: list) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for name_test in names_tests:
        call_data = call_data_test.new(name_test)
        ikb.add(InlineKeyboardButton(text=f'{name_test}',
                                     callback_data=call_data))
    return ikb


def set_IKB_grammar_test() -> InlineKeyboardMarkup:
    dictionary = dict()
    name_test = 'English Level test. Grammar'
    call_data_1 = call_data_test.new(name_test)
    call_data_2 = call_data_test.new('Отмена')
    dictionary[name_test] = call_data_1
    dictionary['Отмена'] = call_data_2
    ikb = set_IKB_many_but(dictionary)
    return ikb


def set_IKB_continue_finish() -> InlineKeyboardMarkup:
    dict_but = {'Остановить тест': '-1', 'Продолжить тест': '0', 'Перезапустить тест': '1'}
    return set_IKB_many_but(dict_but)
