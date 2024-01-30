from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from Utils.From_DB import get_name_survey


# TODO Bot отправлять эту клавиатуру только в личку
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


def set_IKB_many_but(dictionary: dict) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for text, call in dictionary.items():
        ikb.add(InlineKeyboardButton(text=text,
                                     callback_data=call))
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
    list_surveys = get_name_survey()
    for name_test_list in list_surveys:
        name_test = name_test_list[0]
        dictionary[name_test] = f'Run test: {name_test}'

    ikb = set_IKB_many_but(dictionary)
    return ikb


def set_IKB_continue_finish() -> InlineKeyboardMarkup:
    dict_but = {'Остановить тест': '-1', 'Продолжить тест': '0', 'Перезапустить тест': 'r'}
    return set_IKB_many_but(dict_but)
