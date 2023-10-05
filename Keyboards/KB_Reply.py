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


# def set_IKB_run_survey(text_but: str) -> InlineKeyboardMarkup:
#     ikb = InlineKeyboardMarkup(row_width=1)
#     ib1 = InlineKeyboardButton(text=f'Запустить {text_but}',
#                                callback_data='1')
#     ikb.add(ib1)
#     return ikb


def set_IKB_Survey(answers: list) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text=answers[0],
                               callback_data='1')
    ib2 = InlineKeyboardButton(text=answers[1],
                               callback_data='2')
    ib3 = InlineKeyboardButton(text=answers[2],
                               callback_data='3')
    ib4 = InlineKeyboardButton(text=answers[3],
                               callback_data='4')
    ib5 = InlineKeyboardButton(text='Остановить тест',
                               callback_data='0')
    ikb.add(ib1, ib2, ib3, ib4, ib5)
    return ikb


def set_IKB_select_survey() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    try:
        list_surveys = sql.select_db(query.select_SURVEY_NAME_from_SURVEY, None)
        for name_test in list_surveys:
            data = f'Run test: {name_test[0]}'
            ikb.add(InlineKeyboardButton(text=name_test[0],
                                         callback_data=data))

    except Exception as error_exeption:
        print('Error in ikb')
        print(error_exeption)
    return ikb


# TODO добавить клавиатуру для продолжения, перезапуска или окончательной отмены теста
def set_IKB_continue_finish() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text=f'Остановить тест',
                               callback_data='0')
    ib2 = InlineKeyboardButton(text=f'Продолжить тест',
                               callback_data='1')
    ikb.add(ib1, ib2)
    return ikb