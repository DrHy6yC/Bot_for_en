import hashlib
from aiogram import types, Router
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from Utils import Translator, Text_commands


async def inline_translate(inline_query: types.InlineQuery) -> None:
    print('start inline')
    text_inline_query = inline_query.query or 'Введи то что хочешь перевести'
    en_ru = Text_commands.detect_en_simbol(text_inline_query)
    translate_text = Translator.translate_text(text_inline_query, en_ru)
    input_text = f'{text_inline_query} -> {translate_text}'
    input_text_message = InputTextMessageContent(message_text=input_text)
    result_id = hashlib.md5(translate_text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        input_message_content=input_text_message,
        id=result_id,
        title=str(translate_text)
    )
    print(result_id)
    await inline_query.answer(results=[item], cache_time=5, is_personal=True)


def register_inline_handler(router: Router) -> None:
    router.inline_query.register(inline_translate)
