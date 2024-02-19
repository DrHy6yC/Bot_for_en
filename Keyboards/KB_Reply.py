from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def set_buts(text_buts) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for text_but in text_buts:
        button = KeyboardButton(text=text_but)
        kb.add(button)
    return kb.as_markup(resize_keyboard=True)


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
    return ikb.as_markup()


def set_IKB_many_but(dictionary: dict[str, CallbackData]) -> InlineKeyboardMarkup:
    """
        Генерирует inline клавиатуру с несколькими кнопками на которых будут текст, являющийся ключем словаря,
        при нажатии на которую будет отправлен пользовательский CallbackData (call_data) для дальнейшего отлавливания

        Notes:
        ------

        Названия кнопок должны быть уникальными!!! Две кнопки с одним текстом не смогут быть созданны,
        так как название кнопки является ключем словаря

        Parameters:
        ----------
        dictionary - Словарь из текста-ключей и CallbackData

        Returns:
        -------
        InlineKeyboardMarkup - inline клавиатура состоящая из одной кнопки

        """
    ikb = InlineKeyboardBuilder()
    for text, call in dictionary.items():
        ikb.button(text=text, callback_data=call.pack()).adjust(1)
    return ikb.as_markup()
