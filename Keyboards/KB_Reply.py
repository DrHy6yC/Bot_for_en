from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from Callback_datas.our_call_datas import continue_test, restart_test, stop_test
from SQL.models import QuizeAnswersORM
from Callback_datas import select_test, del_message, start_test, cancel_test


def set_but_start() -> ReplyKeyboardMarkup:
    # TODO задать фильтры, что бы разный набор кнопак был у разных пользователей
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Помощь')
    b2 = KeyboardButton(text='Пройти тест')
    b3 = KeyboardButton(text='Узнать уровень')
    kb.add(b3, b1, b2)
    return kb


def set_IKB_one_but(text: str, call_data: CallbackData) -> InlineKeyboardMarkup:
    """
    Генерирует inline клавиатуру с одной кнопкой на которой будет текст полученный из параметров(text),
    при нажатии на которую будет отправлен пользовательский CallbackData (call_data) для дальнейшего отлавливания

    Parameters:
    ----------
    text - Строка которая будет отображатся на кнопке

    call_data - CallbackData которую нужно будет ловить call_data.filter()

    Returns:
    -------
    InlineKeyboardMarkup - inline клавиатура состоящая из одной кнопки

    """
    ikb = InlineKeyboardMarkup(row_width=1)
    ib = InlineKeyboardButton(text=text,
                              callback_data=call_data)
    ikb.add(ib)
    return ikb


def set_IKB_many_but(dictionary: dict[str, CallbackData]) -> InlineKeyboardMarkup:
    """
        Генерирует inline клавиатуру с одной кнопкой на которой будет текст полученный из параметров(text),
        при нажатии на которую будет отправлен пользовательский CallbackData (call_data) для дальнейшего отлавливания

        Parameters:
        ----------
        text - Строка которая будет отображатся на кнопке

        call_data - CallbackData которую нужно будет ловить call_data.filter()

        Returns:
        -------
        InlineKeyboardMarkup - inline клавиатура состоящая из одной кнопки

        """
    ikb = InlineKeyboardMarkup(row_width=1)
    for text, call in dictionary.items():
        ikb.add(InlineKeyboardButton(text=text,
                                     callback_data=call))
    return ikb


def set_IKB_Survey(running_test_id: int, answers: list[QuizeAnswersORM]) -> InlineKeyboardMarkup:
    dictionary = dict()
    for answer in answers:
        call_data = start_test.new(answer.ID)
        dictionary[answer.ANSWER_TEXT] = call_data
    call_data_x = stop_test.new(running_test_id)
    dictionary['Остановить тест'] = call_data_x
    ikb = set_IKB_many_but(dictionary)
    return ikb


# def set_IKB_select_survey(dictionary) -> InlineKeyboardMarkup:
#     ikb = set_IKB_many_but(dictionary)
#     return ikb


def set_IKB_select_survey(names_tests: list) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    for name_test in names_tests:
        call_data = select_test.new(name_test)
        ikb.add(InlineKeyboardButton(text=f'{name_test}',
                                     callback_data=call_data))
    call_data = del_message.new()
    ikb.add(InlineKeyboardButton(text=f'Отмена',
                                 callback_data=call_data))
    return ikb


def set_IKB_grammar_test() -> InlineKeyboardMarkup:
    dictionary = dict()
    # TODO сделать выбор теста по умолчанию
    name_test = 'English Level test. Grammar'
    call_data_1 = select_test.new(name_test)
    call_data_2 = del_message.new()
    dictionary[name_test] = call_data_1
    dictionary['Отмена'] = call_data_2
    ikb = set_IKB_many_but(dictionary)
    return ikb


def set_IKB_stop_test(user_test_id: int) -> InlineKeyboardMarkup:
    dict_but = {
        'Остановить тест': cancel_test.new(user_test_id),
        'Продолжить тест': continue_test.new(user_test_id),
        'Перезапустить тест': restart_test.new(user_test_id)
    }
    ikb = set_IKB_many_but(dict_but)
    return ikb
