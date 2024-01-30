from aiogram import types, Dispatcher

from magic_filter import F
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot
from Keyboards import KB_Reply
from Utils.From_DB import get_id_survey, get_answer, get_question, set_user_survey_get_id_user_survey
from Utils.From_DB import get_one_answer, get_count_question, get_is_user_status_survey, get_user_survey


async def delete_message(callback: types.CallbackQuery) -> None:
    print('Message delete')
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    return await callback.answer()


async def test_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test 1. Получать/сохранять из/и бд информацию о пользователе и тесте
    name_test = callback.data.replace("Run test: ", "")
    # TODO SQL 1. get_is_user_status_survey(user_id: int, status: int) -> bool
    user_id = callback.from_user.id
    # TODO Test -> TODO SQL 1.1. Создание условии проверки: у одного пользователя может быть только один активный тест
    if get_is_user_status_survey(int(user_id), 1):
        await callback.answer('Уже есть запущенный тест', show_alert=True)
    else:
        # TODO SQL 1.2. set_user_survey_get_id_user_survey(user_id, test_id, status=1)
        # TODO Test 1 -> TODO SQL 1.2. Убрать state.update_data
        id_test = get_id_survey(name_test)
        print(id_test, user_id, 1)
        set_user_survey_get_id_user_survey(user_id, id_test, 1)
        # await state.update_data(name_test=name_test, id_test=id_test)
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


# TODO Sql+Test 1. получать/сохранять из/и бд информацию о пользователе и тесте
async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    id_chat = callback.message.chat.id
    user_id = callback.from_user.id
    # TODO Sql 2. get_user_survey(user_id, status)
    test_info = get_user_survey(user_id, 1)
    # TODO Test -> TODO Sql 2. Убрать data
    data = await state.get_data()
    test_id = data['id_test']
    # test_id = test_info[2]
    MAX_QUESTION_SURVEY = get_count_question(int(test_id))
    question_num = data.get('question_num', 0) #test_info[4]
    question_num += 1
    answer_user = str(callback.data)
    await state.update_data(question_num=question_num, answer_user=answer_user)
    answers_list = get_answer(question_num, test_id)
    answers = list()
    for i in answers_list:
        answers.append(i[0])
    await bot.edit_message_reply_markup(
        chat_id=id_chat,
        message_id=callback.message.message_id,
        reply_markup=None)
    if question_num == 1:
        question = get_question(question_num, test_id)
        await state.update_data(question=question)
        if answer_user in ['1', '2', '3', '4']:
            await bot.send_message(chat_id=id_chat,
                                   text=question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))
    elif MAX_QUESTION_SURVEY >= question_num > 1:
        new_question = get_question(question_num, test_id)
        question = data.get('question')
        await state.update_data(question=new_question)
        answer_user_text = get_one_answer(question_num - 1, test_id, answer_user)
        text_q = question.replace('______', f'<u><em>{answer_user_text}</em></u>')
        # Ошибка если текст не изменялся
        if answer_user_text == text_q:
            await bot.edit_message_text(
                chat_id=id_chat,
                message_id=callback.message.message_id,
                parse_mode="html",
                text=text_q)
        if answer_user in ['1', '2', '3', '4']:
            await bot.send_message(chat_id=id_chat,
                                   text=new_question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))
        else:
            await FSMTest.test_revoked.set()
    elif question_num == MAX_QUESTION_SURVEY + 1:
        question = data.get('question')
        answer_user_text = get_one_answer(question_num - 1, test_id, answer_user)
        text_q = question.replace('______', f'<u><em>{answer_user_text}</em></u>')
        await bot.edit_message_text(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=text_q)
        await FSMTest.test_completed.set()
        await bot.edit_message_reply_markup(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            reply_markup=KB_Reply.set_IKB_one_but('Посмотреть результаты', 'view_result'))
    else:
        print('ERROR')
    await callback.answer()


async def test_revoked(callback: types.CallbackQuery) -> None:
    # TODO Sql+Test. Смена статуса теста в БД
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
    # TODO Sql+Test. Смена статуса теста в БД
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест Прерван\nРезультат - хз')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать продолжение теста
async def test_continue(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Выбор из ранее запущенных (остановленных и прерванных)
    pass


# TODO Bot+Sql+Test 2. Реализация расчета результата
async def test_completed(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест закончен\nРезультат - хз')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать перезапуск теста
async def test_restart(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Выбор из ранее запущенных (остановленных и прерванных)
    pass


def register_call_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(test_handler, F.data.startswith('Run test: '), state=FSMTest.test_handler)
    dp.register_message_handler(test_progress, state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_revoked, text='-1', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text=['1', '2', '3', '4'], state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_completed, state=FSMTest.test_completed)
    dp.register_callback_query_handler(test_continue, state=FSMTest.test_revoked, text='0')
    dp.register_callback_query_handler(test_canceled, state=FSMTest.test_revoked, text='-1')
    dp.register_callback_query_handler(delete_message, state="*", text='delete_message')
    dp.register_callback_query_handler(test_restart, state=FSMTest.test_revoked, text='r')
