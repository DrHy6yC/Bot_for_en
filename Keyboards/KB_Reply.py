from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# from Callback_datas.our_call_datas import continue_test, restart_test, stop_test
from SQL.models import QuizeAnswersORM
# from Callback_datas import select_test, del_message, start_test, cancel_test


# def set_kb(callback: CallbackData):
#     builder = InlineKeyboardBuilder()
#     builder.button(
#         text='Ok',
#         callback_data=callback.pack(),
#     )
#     return builder.as_markup()


def set_buts(text_buts) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for text_btn in text_buts:
        button = KeyboardButton(text=text_btn)
        kb.add(button)
    return kb.as_markup()


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
    ikb = InlineKeyboardBuilder()
    ikb.button(text=text, callback_data=call_data.pack())
    ikb.as_markup()
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
    ikb = InlineKeyboardBuilder()
    for text, call in dictionary.items():
        ikb.button(text=text, callback_data=call.pack())
    return ikb.as_markup()


# def set_IKB_Survey(running_test_id: int, answers: list[QuizeAnswersORM]) -> InlineKeyboardMarkup:
#     dictionary = dict()
#     for answer in answers:
#         call_data = start_test.new(answer.ID)
#         dictionary[answer.ANSWER_TEXT] = call_data
#     call_data_x = stop_test.new(running_test_id)
#     dictionary['Остановить тест'] = call_data_x
#     ikb = set_IKB_many_but(dictionary)
#     return ikb


# def set_IKB_select_survey(dictionary) -> InlineKeyboardMarkup:
#     ikb = set_IKB_many_but(dictionary)
#     return ikb


# def set_IKB_select_survey(names_tests: list) -> InlineKeyboardMarkup:
#     ikb = InlineKeyboardMarkup(row_width=1)
#     for name_test in names_tests:
#         call_data = select_test.new(name_test)
#         ikb.add(InlineKeyboardButton(text=f'{name_test}',
#                                      callback_data=call_data))
#     call_data = del_message.new()
#     ikb.add(InlineKeyboardButton(text=f'Отмена',
#                                  callback_data=call_data))
#     return ikb

#
# def set_IKB_grammar_test() -> InlineKeyboardMarkup:
#     dictionary = dict()
#     # TODO сделать выбор теста по умолчанию
#     name_test = 'English Level test. Grammar'
#     call_data_1 = select_test.new(name_test)
#     call_data_2 = del_message.new()
#     dictionary[name_test] = call_data_1
#     dictionary['Отмена'] = call_data_2
#     ikb = set_IKB_many_but(dictionary)
#     return ikb
#
#
# def set_IKB_stop_test(user_test_id: int) -> InlineKeyboardMarkup:
#     dict_but = {
#         'Остановить тест': cancel_test.new(user_test_id),
#         'Продолжить тест': continue_test.new(user_test_id),
#         'Перезапустить тест': restart_test.new(user_test_id)
#     }
#     ikb = set_IKB_many_but(dict_but)
#     return ikb
