from icecream import ic
from aiogram import types, Dispatcher

from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot
from SQL.models import UserQuizzesORM
from SQL import orm
from Callback_datas.our_call_datas import call_data_test, call_data_cancel
from Keyboards import KB_Reply


async def delete_message(callback: types.CallbackQuery, state: FSMContext) -> None:
    ic('Message delete')
    ic(await state.get_state())
    if await state.get_state() != 'FSMTest:test_revoked':
        await state.finish()
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    # await callback.answer()


async def test_handler(callback: types.CallbackQuery, callback_data: dict, state: FSMContext) -> None:
    """
    Notes:
        Убедиться что пользователь нажимал старт и зарегистрирован в БД бота!

    Parameters
    ----------
    callback
    callback_data
    state

    Returns
    -------

    """

    # await delete_message(callback, state)
    name_test = callback_data.get('name_test')
    user_tg_id = callback.from_user.id
    if await orm.async_get_is_user_status_test(int(user_tg_id), 1):
        test_info = await orm.async_get_user_test_by_user_tg_id_and_status(user_tg_id, 1)
        user_test_id = test_info.ID
        await callback.answer('Уже есть запущенный тест, теперь он остановлен', show_alert=True)
        await orm.async_set_user_test_status(user_test_id, 3)
        ic('Change state = 3')
        ic(await state.get_state())
        ic(str(callback.data))

    else:
        id_test = await orm.async_get_id_test(name_test)
        ic(user_tg_id, id_test, name_test)
        user_test = UserQuizzesORM(
            ID_USER_TG=user_tg_id,
            ID_QUIZE=id_test,
            QUIZE_STATUS=1,
            QUESTION_NUMBER=1
        )
        await orm.async_insert_data_list_to_bd([user_test])
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
    user_tg_id = callback.from_user.id
    test_info = await orm.async_get_user_test_by_user_tg_id_and_status(user_tg_id, 1)
    user_test_id = test_info.ID
    if answer_user == '-1':
        # TODO переделать Callback_data
        await orm.async_set_user_test_status(user_test_id, 3)
        ic('Change state = 3')
        ic(await state.get_state())
        ic(str(callback.data))
        await FSMTest.test_revoked.set()
        ic(await state.get_state())
        await delete_message(callback, state)
        await bot.send_message(chat_id=id_chat,
                               text='Тест приостановлен',
                               reply_markup=KB_Reply.set_IKB_continue_finish())
        # await callback.answer()
    else:
        test_id = test_info.ID_QUIZE
        MAX_QUESTION_SURVEY = await orm.async_get_count_question_test(test_id)
        question_num = test_info.QUESTION_NUMBER
        # set_question_num(question_num, user_test_id)
        answers = await orm.async_get_answers_by_id_test_and_num_question(question_num, test_id)
        # for i in answers:
        #     answers.append(i[0])
        await bot.edit_message_reply_markup(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            reply_markup=None)
        if question_num == 1:
            ic()
            question = await orm.async_get_question_by_id_test_num_question(
                test_info.ID_QUIZE, test_info.QUESTION_NUMBER
            )
            await bot.send_message(chat_id=id_chat,
                                   text=question,
                                   reply_markup=KB_Reply.set_IKB_Survey(answers))

        elif MAX_QUESTION_SURVEY >= question_num > 1:
            ic()
            answer_id = get_answer_id(test_id, question_num, int(answer_user))
            set_user_answer(answer_id, user_test_id, question_num - 1)
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
            ic()
            answer_id = get_answer_id(test_id, question_num-1, int(answer_user))
            ic(answer_id)
            set_user_answer(answer_id, user_test_id, question_num - 1)
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
            ic('Change state = 5')
            await bot.edit_message_reply_markup(
                chat_id=id_chat,
                message_id=callback.message.message_id,
                reply_markup=KB_Reply.set_IKB_one_but('Посмотреть результаты', 'view_result'))
        else:
            ic('ERROR')
        question_num += 1
        set_question_num(question_num, user_test_id)
        balls_now = comparison_answer(user_test_id)
        ic(balls_now)
        set_balls(user_test_id, balls_now)
    await callback.answer()


async def test_canceled(callback: types.CallbackQuery, state: FSMContext) -> None:
    ic(await state.get_state())
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    user_id = callback.from_user.id
    test_info = get_user_survey(user_id, 3)[0]
    user_test_id = test_info[0]
    ball = get_balls(user_test_id)
    test_id = test_info[2]
    MAX_QUESTION_SURVEY = get_count_question(int(test_id))
    percent = float(ball) / float(MAX_QUESTION_SURVEY) * 100
    percent = round(percent, 2)
    set_user_survey_status_test(user_test_id, 4)
    ic(await state.get_state())
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=f'Тест отменен\n'
                                f'Результат: {percent}%\n'
                                f'{ball} правильных ответов\n'
                                f'из {MAX_QUESTION_SURVEY} всех вопросов\n'
                                f'"Это уровень: {getLevelUser(percent)}')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать продолжение теста
async def test_continue(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Выбор из ранее запущенных (остановленных и прерванных)
    # user_id = callback.from_user.id
    # test_info = get_user_survey(user_id, 1)[0]
    # user_test_id = test_info[0]
    # set_user_survey_status_test(user_test_id, 4)
    # FSMTest.test_continue.set()
    # ic(await state.get_state())
    await callback.answer('Сейчас можно только остановить тест', show_alert=True)


async def test_completed(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    test_info = get_user_survey(user_id, 5)[0]
    user_test_id = test_info[0]
    ball = get_balls(user_test_id)
    test_id = test_info[2]
    MAX_QUESTION_SURVEY = get_count_question(int(test_id))
    percent = float(ball)/float(MAX_QUESTION_SURVEY) * 100
    percent = round(percent, 2)
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=f'Тест закончен\n'
                                f'Результат: {percent}%\n'
                                f'{ball} правильных ответов\n'
                                f'из {MAX_QUESTION_SURVEY} всех вопросов\n'
                                f'"Это уровень: {getLevelUser(percent)}')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать перезапуск теста
async def test_restart(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO Sql+Test. Выбор из ранее запущенных (остановленных и прерванных)
    await callback.answer('Сейчас можно только остановить тест', show_alert=True)


def register_call_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(delete_message, call_data_test.filter(name_test='Отмена'), state="*")
    dp.register_callback_query_handler(delete_message, call_data_cancel.filter(), state="*")
    # dp.register_callback_query_handler(delete_message, state="*", text='delete_message')
    dp.register_callback_query_handler(test_handler, call_data_test.filter(), state=FSMTest.test_handler)
    dp.register_callback_query_handler(test_progress, text=['-1', '1', '2', '3', '4'], state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_completed, state=FSMTest.test_completed)
    dp.register_callback_query_handler(test_continue, state=FSMTest.test_revoked, text='0')
    dp.register_callback_query_handler(test_canceled, state=FSMTest.test_revoked, text='-1')
    dp.register_callback_query_handler(test_restart, state=FSMTest.test_revoked, text='1')

