from aiogram import types, Dispatcher
from Create_bot import bot, MY_ID, sql_bot
from Keyboards import KB_Reply



async def test_handler(callback: types.CallbackQuery) -> None:
    # Отправить в БД ид теста
    print('callback data: ', callback.data)
    try:
        name_test = callback.data.replace("Run test: ", "")
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=f'Выбран тест: {name_test}')
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=KB_Reply.set_IKB_run_survey(name_test))
    except Exception as error_exception:
        await bot.send_message(chat_id=MY_ID,
                               text=str(error_exception))


async def run_test(callback: types.CallbackQuery) -> None:
    print('callback data: ', callback.data)
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await test_progress(callback)


async def test_progress(callback: types.CallbackQuery) -> None:
    # получить из бд ид теста
    id_survey = 28
    try:
        print('callback data: ', callback)
        NUM_QUESTION = 1
        cond = {'SURVEY_ID': id_survey, 'NUMBER_QUESTION': NUM_QUESTION}
        result_to_bd = sql_bot.select_table_with_condition('SURVEYS_ANSWERS', cond)
        question = result_to_bd[3]
        answers = [result_to_bd[4], result_to_bd[5], result_to_bd[6], result_to_bd[7]]
        answer_text = question
        answer_user = answers[int(callback.data)]
        question_insert_answer = answer_text.replace('______', f'<u><em>{answer_user}</em></u>')
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=None)
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=question_insert_answer)
        # num_add()
        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=question,
            reply_markup=KB_Reply.set_IKB_Survey(answers))
    except Exception as error_except:
        await bot.send_message(
            chat_id=callback.message.chat.id,
            text="Вопросы кончились",
            reply_markup=None)


def register_call_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(test_handler, text='Run test: Проверочный тест')
    dp.register_callback_query_handler(run_test, text='0')
    dp.register_callback_query_handler(test_progress, text='1')
    dp.register_callback_query_handler(test_progress, text='2')
    dp.register_callback_query_handler(test_progress, text='3')
    dp.register_callback_query_handler(test_progress, text='4')


