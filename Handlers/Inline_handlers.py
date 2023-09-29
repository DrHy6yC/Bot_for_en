import hashlib
from aiogram import types, Dispatcher
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from Utils import Translator, Text_commands


async def inline_echo(inline_query: types.InlineQuery) -> None:
    try:
        text_inline_query = inline_query.query or 'Введи то что хочешь перевести'
        en_ru = Text_commands.detect_en_simbol(text_inline_query)
        translate_text = Translator.translate_text(text_inline_query, en_ru)
        input_text = f'{text_inline_query} -> {translate_text}'
        input_text_message = InputTextMessageContent(input_text)
        result_id = hashlib.md5(translate_text.encode()).hexdigest()
        # print(inline_query.from_user.id, input_text, sep='\n')

        item = InlineQueryResultArticle(
            input_message_content=input_text_message,
            id=result_id,
            title=str(translate_text)
        )
        # print(result_id)
        await inline_query.answer([item], cache_time=1, is_personal=True)
    except Exception as error_exception:
        print(error_exception)


def register_inline_handler(dp: Dispatcher) -> None:
    dp.register_inline_handler(inline_echo)

