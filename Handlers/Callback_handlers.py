from aiogram import types, Dispatcher

from magic_filter import F
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot
from Keyboards import KB_Reply
from Utils.From_DB import get_id_survey, get_answer, get_question_by_id_question, set_user_survey_get_id_user_survey, \
    set_question_num, get_one_answer, get_count_question, get_is_user_status_survey, get_user_survey, \
    set_user_survey_status_test, set_user_answer, get_answer_id


async def delete_message(callback: types.CallbackQuery) -> None:
    print('Message delete')
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    return await callback.answer()


async def test_handler(callback: types.CallbackQuery) -> None:
    name_test = callback.data.replace("Run test: ", "")
    user_id = callback.from_user.id
    if get_is_user_status_survey(int(user_id), 1):
        await callback.answer('Уже есть запущенный тест', show_alert=True)
    else:
        id_test = get_id_survey(name_test)
        user_test_id = set_user_survey_get_id_user_survey(user_id, id_test, 1)
        set_question_num(1, user_test_id)
        await FSMTest.test_progressed.set()
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=f'Выбран тест: {name_test}')
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=KB_Reply.set_IKB_one_but(f'Запустить {name_test}', '1'))
        await callback.answer()


async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    answer_user = str(callback.data)
    id_chat = callback.message.chat.id
    user_id = callback.from_user.id
    test_info = get_user_survey(user_id, 1)
    user_test_id = test_info[0]
    if answer_user == '-1':
        set_user_survey_status_test(user_test_id, 3)
        await FSMTest.test_revoked.set()
        await delete_message(callback)
        await bot.send_message(chat_id=id_chat,
                               text='Тест приостановлен',
                               reply_markup=KB_Reply.set_IKB_continue_finish())
        print('Change state = 3')
        print(await state.get_state())
        print(str(callback.data))
    else:
        test_id = test_info[2]
        MAX_QUESTION_SURVEY = get_count_question(int(test_id))
        question_num = test_info[4]
        set_question_num(question_num, user_test_id)
        answers_list = get_answer(question_num, test_id)
        answers = list()
        for i in answers_list:
            answers.append(i[0])
        await bot.edit_message_reply_markup(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            reply_markup=None)
        if question_num == 1:
            answer_id = get_answer_id(test_id, question_num, int(answer_user))
            set_user_answer(answer_id, user_test_id, question_num)
            question = get_question_by_id_question(test_info[5])
            await bot.send_message(chat_id=id_chat,
                                   text=question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))

        elif MAX_QUESTION_SURVEY >= question_num > 1:
            answer_id = get_answer_id(test_id, question_num, int(answer_user))
            set_user_answer(answer_id, user_test_id, question_num)
            question = get_question_by_id_question(test_info[5])
            previous_question = get_question_by_id_question(test_info[6])
            answer_user_text = get_one_answer(question_num - 1, test_id, int(answer_user))
            text_q = previous_question.replace('______', f'<u><em>{answer_user_text}</em></u>')
            if previous_question != text_q:
                await bot.edit_message_text(
                    chat_id=id_chat,
                    message_id=callback.message.message_id,
                    parse_mode="html",
                    text=text_q)
            await bot.send_message(chat_id=id_chat,
                                   text=question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))
        elif question_num == MAX_QUESTION_SURVEY + 1:
            previous_question = get_question_by_id_question(test_info[6])
            answer_user_text = get_one_answer(question_num - 1, test_id, int(answer_user))
            text_q = previous_question.replace('______', f'<u><em>{answer_user_text}</em></u>')
            if previous_question != text_q:
                await bot.edit_message_text(
                    chat_id=id_chat,
                    message_id=callback.message.message_id,
                    parse_mode="html",
                    text=text_q)
            await FSMTest.test_completed.set()
            set_user_survey_status_test(user_test_id, 5)
            print('Change state = 5')
            await bot.edit_message_reply_markup(
                chat_id=id_chat,
                message_id=callback.message.message_id,
                reply_markup=KB_Reply.set_IKB_one_but('Посмотреть результаты', 'view_result'))
        else:
            print('ERROR')
        question_num += 1
        set_question_num(question_num, user_test_id)
    await callback.answer()


async def test_canceled(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Смена статуса теста в БД
    print(await state.get_state())
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    user_id = callback.from_user.id
    test_info = get_user_survey(user_id, 3)
    user_test_id = test_info[0]
    set_user_survey_status_test(user_test_id, 4)
    print(await state.get_state())
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест отменен\nРезультат - хз')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать продолжение теста
async def test_continue(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Выбор из ранее запущенных (остановленных и прерванных)
    # user_id = callback.from_user.id
    # test_info = get_user_survey(user_id, 1)
    # user_test_id = test_info[0]
    # set_user_survey_status_test(user_test_id, 4)
    # FSMTest.test_continue.set()
    # print(await state.get_state())
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
    dp.register_callback_query_handler(test_progress, text=['-1', '1', '2', '3', '4'], state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_completed, state=FSMTest.test_completed)
    dp.register_callback_query_handler(test_continue, state=FSMTest.test_revoked, text='0')
    dp.register_callback_query_handler(test_canceled, state=FSMTest.test_revoked, text='-1')
    dp.register_callback_query_handler(delete_message, state="*", text='delete_message')
    dp.register_callback_query_handler(test_restart, state=FSMTest.test_revoked, text='1')
