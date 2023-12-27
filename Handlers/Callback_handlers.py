
from aiogram import types, Dispatcher

from magic_filter import F
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot, sql
from Keyboards import KB_Reply
from Utils import SQL_querys as query


async def delete_message(callback: types.CallbackQuery) -> None:
    print('Message delete')
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    return await callback.answer()


async def view_result_test(callback: types.CallbackQuery) -> None:
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Результат ХЗ',
                           reply_markup=None)


async def test_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    # # Отправить в БД ид теста
    print(await state.get_state() == 'FSMTest:test_handler')
    name_test = callback.data.replace("Run test: ", "")
    id_test = sql.select_db_one(
        query=query.select_SURVEY_ID_from_SURVEY_by_SURVEY_NAME,
        data={'SURVEY_NAME': name_test}
    )
    await state.update_data(name_test=name_test, id_test=id_test)
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        parse_mode="html",
        text=f'Выбран тест: {name_test}')
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=KB_Reply.set_IKB_one_but(f'Запустить {name_test}', '1'))
    await FSMTest.test_progressed.set()
    await callback.answer()


async def get_data_bd(test_id: int, question_num: int, data: dict, answer_user) -> dict:
    max_question = sql.select_db_one(
        query.select_COUNT_QUESTION_from_SURVEYS_QUESTIONS_by_SURVEY_ID,
        {'SURVEY_ID': test_id})
    new_question = sql.select_db_one(
        query.select_SURVEY_QUESTION_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID,
        {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num})
    question = data.get('question', new_question)
    answer_user_text = sql.select_db_one(
        query.select_ANSWER_USER_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID_and_NUMBER_ANSWER,
        {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num, 'NUMBER_ANSWER': answer_user})
    text_q = question.replace('______', f'<u><em>{answer_user_text}</em></u>')
    answers_list = sql.select_db(
        query.select_ANSWERS_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID,
        {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num})
    return {'max_question': max_question, 'text_q': text_q, 'answers_list': answers_list}


# TODO получать из бд информацию о пользователе и тесте
async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    id_chat = callback.message.chat.id
    data = await state.get_data()
    print(data)
    test_id = data['id_test']
    question_num = data.get('question_num', 0)
    print(question_num)
    question_num += 1
    print(question_num)
    answer_user = str(callback.data)
    await state.update_data(question_num=question_num, answer_user=answer_user)
    print(await state.get_data())
    answers_list = sql.select_db(
        query.select_ANSWERS_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID,
        {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num})
    print(answers_list)
    answers = list()
    print(answers)
    for i in answers_list:
        answers.append(i[0])
    await bot.edit_message_reply_markup(
        chat_id=id_chat,
        message_id=callback.message.message_id,
        reply_markup=None)
    if question_num == 1:
        print(question_num)
        question = sql.select_db_one(
            query.select_SURVEY_QUESTION_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID,
            {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num})
        await state.update_data(question=question)
        if answer_user in ['1', '2', '3', '4']:
            print(question)
            await bot.send_message(chat_id=id_chat,
                                   text=question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))
    elif 7 >= question_num > 1:
        print(question_num)
        new_question = sql.select_db_one(
            query.select_SURVEY_QUESTION_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID,
            {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num})
        question = data.get('question')
        await state.update_data(question=new_question)
        answer_user_text = sql.select_db_one(
            query.select_ANSWER_USER_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID_and_NUMBER_ANSWER,
            {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num - 1, 'NUMBER_ANSWER': answer_user})
        text_q = question.replace('______', f'<u><em>{answer_user_text}</em></u>')
        await bot.edit_message_text(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=text_q)
        print('answer_user: ', answer_user)
        if answer_user in ['1', '2', '3', '4']:
            print(new_question)
            await bot.send_message(chat_id=id_chat,
                                   text=new_question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))
        else:
            await FSMTest.test_revoked.set()
    elif question_num == 8:
        print(question_num)
        question = data.get('question')
        answer_user_text = sql.select_db_one(
            query.select_ANSWER_USER_from_SURVEYS_ANSWERS_by_NUMBER_QUESTION_and_SURVEY_ID_and_NUMBER_ANSWER,
            {'SURVEY_ID': test_id, 'NUMBER_QUESTION': question_num - 1, 'NUMBER_ANSWER': answer_user})
        text_q = question.replace('______', f'<u><em>{answer_user_text}</em></u>')
        await bot.edit_message_text(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=text_q)
        print('answer_user: ', answer_user)
        await FSMTest.test_completed.set()
        await bot.edit_message_reply_markup(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            reply_markup=KB_Reply.set_IKB_one_but('Посмотреть результаты', 'view_result'))
    else:
        print('ERROR')
    await callback.answer()


async def test_revoked(callback: types.CallbackQuery) -> None:
    await FSMTest.test_revoked.set()
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест прерван',
                           reply_markup=KB_Reply.set_IKB_continue_finish())
    await callback.answer()


async def test_canceled(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест Прерван\nРезультат - хз')
    await callback.answer()


async def test_continue(callback: types.CallbackQuery) -> None:
    pass
    # await bot.edit_message_reply_markup(
    #     chat_id=callback.message.chat.id,
    #     message_id=callback.message.message_id,
    #     reply_markup=None)
    # await FSMTest.test_progressed.set()
    # await callback.answer()
    # await bot.send_message(chat_id=callback.message.chat.id,
    #                        text='Продолжаем тест')


async def test_completed(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест закончен\nРезультат - хз')
    await callback.answer()


def register_call_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(test_handler, F.data.startswith('Run test: '), state=FSMTest.test_handler)
    dp.register_message_handler(test_progress, state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_revoked, text='-1', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text=['1', '2', '3', '4'], state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_completed, state=FSMTest.test_completed)
    # dp.register_callback_query_handler(test_continue, state=FSMTest.test_continue)
    dp.register_callback_query_handler(test_canceled, state=FSMTest.test_revoked)
    dp.register_callback_query_handler(delete_message, state="*", text='delete_message')
