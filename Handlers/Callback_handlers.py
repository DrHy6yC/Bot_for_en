from icecream import ic
from aiogram import types, Router

from Callback_datas import DelMessageCal, ProgressTestCal, SelectTestCal, CanceledTestCal, ViewResultTestCal
from Create_bot import bot
from SQL.models import UserQuizzesORM, UserAnswersORM
from SQL import orm
from Keyboards import set_IKB_many_but, set_IKB_one_but


async def delete_message(callback: types.CallbackQuery) -> None:
    ic('Message delete')
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)


async def test_handler(callback: types.CallbackQuery, callback_data: SelectTestCal) -> None:
    """
    Notes:
        Убедиться что пользователь нажимал старт и зарегистрирован в БД бота!

    """

    name_test = callback_data.name_test
    user_tg_id = callback.from_user.id
    if await orm.async_get_is_user_status_test(int(user_tg_id), 2):
        run_test = await orm.async_get_user_test_by_user_tg_id_and_status(user_tg_id, 2)
        user_test_id = run_test.ID
        await callback.answer('Уже есть запущенный тест, теперь он остановлен', show_alert=True)
        await orm.async_set_user_test_status(user_test_id, 3)
    else:
        id_test = await orm.async_get_id_test(name_test)
        user_test = UserQuizzesORM(
            ID_USER_TG=user_tg_id,
            ID_QUIZE=id_test,
            QUIZE_STATUS=1,
            QUESTION_NUMBER=0
        )
        await orm.async_insert_data_list_to_bd([user_test])
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=f'Выбран тест: {name_test}')
        run_test = await orm.async_get_user_test_by_user_tg_id_and_status(user_tg_id, 1)
        dict_str_cal = dict()
        dict_str_cal[f'Запустить {name_test}'] = ProgressTestCal(id_answer='0')
        dict_str_cal['Отмена'] = CanceledTestCal(id_user_test=run_test.ID)

        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=set_IKB_many_but(dict_str_cal)
        )
        await callback.answer()


async def test_progress(callback: types.CallbackQuery, callback_data: ProgressTestCal) -> None:
    ic()
    id_user_answer = int(callback_data.id_answer)
    message_id = callback.message.message_id
    user_tg_id = callback.from_user.id
    running_test = await orm.async_get_user_test_by_user_tg_id_and_status(user_tg_id, 1)
    running_test_id = running_test.ID
    quize_id = running_test.ID_QUIZE
    question_num = running_test.QUESTION_NUMBER
    MAX_QUESTION_SURVEY = await orm.async_get_count_question_test(quize_id)
    if id_user_answer != 0:
        answer_user = UserAnswersORM(
            ID_USER_TG=user_tg_id,
            ID_USER_QUIZE=running_test_id,
            ID_ANSWER=id_user_answer,
            QUESTION_NUMBER=question_num
        )
        await orm.async_insert_data_list_to_bd([answer_user])
        true_answer = await orm.async_get_true_answer(quize_id, question_num)
        ic(id_user_answer, true_answer.ID_ANSWER)
        score = running_test.QUIZE_SCORE
        if id_user_answer == true_answer.ID_ANSWER:
            score += 1
        await orm.async_update_running_test_score(running_test_id, score)
    if question_num == 0:
        ic()
        ic(id_user_answer)
        await bot.edit_message_reply_markup(
            chat_id=user_tg_id,
            message_id=message_id,
            reply_markup=None
        )
        question_num += 1
        await orm.async_update_running_test_num_question(running_test_id, question_num)
        answers = await orm.async_get_answers_by_id_test_and_num_question(quize_id, question_num)
        question_text = await orm.async_get_question_by_id_test_num_question(quize_id, question_num)
        ic(running_test_id)
        dict_buts = dict()
        for answer in answers:
            dict_buts[answer.ANSWER_TEXT] = ProgressTestCal(id_answer=str(answer.ID))
        dict_buts['Отмена'] = CanceledTestCal(id_user_test=str(running_test_id))
        await bot.send_message(
            chat_id=user_tg_id,
            text=question_text,
            reply_markup=set_IKB_many_but(dict_buts)
        )
    elif 1 <= question_num < MAX_QUESTION_SURVEY:
        ic()
        ic(id_user_answer)
        question_text = await orm.async_get_question_by_id_test_num_question(quize_id, question_num)
        answer_user_text = await orm.async_get_answer_text_by_id(id_user_answer)
        text_q = question_text.replace('______', f'<u><em>{answer_user_text}</em></u>')
        await bot.edit_message_text(
            chat_id=user_tg_id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=text_q
        )
        question_num += 1
        await orm.async_update_running_test_num_question(running_test_id, question_num)
        answers = await orm.async_get_answers_by_id_test_and_num_question(quize_id, question_num)
        question_text = await orm.async_get_question_by_id_test_num_question(quize_id, question_num)
        dict_buts = dict()
        for answer in answers:
            dict_buts[answer.ANSWER_TEXT] = ProgressTestCal(id_answer=str(answer.ID))
        dict_buts['Отмена'] = CanceledTestCal(id_user_test=str(running_test_id))
        await bot.send_message(
            chat_id=user_tg_id,
            text=question_text,
            reply_markup=set_IKB_many_but(dict_buts)
        )
    else:
        ic()
        ic(id_user_answer)
        question_text = await orm.async_get_question_by_id_test_num_question(quize_id, question_num)
        answer_user_text = await orm.async_get_answer_text_by_id(id_user_answer)
        text_q = question_text.replace('______', f'<u><em>{answer_user_text}</em></u>')
        await bot.edit_message_text(
            chat_id=user_tg_id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=text_q
        )
        await orm.async_set_user_test_status(running_test_id, 5)
        await bot.send_message(
            chat_id=user_tg_id,
            text='Тест завершён',
            reply_markup=set_IKB_one_but(
                text='Посмотреть результаты',
                call_data=ViewResultTestCal(id_user_test=running_test_id)
            )
        )
    ic()
    ic(question_num, id_user_answer)
    ic(id_user_answer)
    await callback.answer()


# async def test_stopped(callback: types.CallbackQuery, callback_data: ) -> None:
#     user_tg_id = callback.from_user.id
#     user_tset_id = int(callback_data.get('id_user_test'))
#     await bot.edit_message_reply_markup(
#         chat_id=user_tg_id,
#         message_id=callback.message.message_id,
#         reply_markup=KB_Reply.set_IKB_stop_test(user_tset_id)
#     )


async def test_canceled(callback: types.CallbackQuery, callback_data: CanceledTestCal) -> None:
    user_tg_id = callback.from_user.id
    await bot.edit_message_reply_markup(
        chat_id=user_tg_id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    user_tset_id = int(callback_data.id_user_test)
    await orm.async_set_user_test_status(user_tset_id, 3)
    run_test = await orm.async_get_user_test_by_id(user_tset_id)
    ic(run_test.ID)
    points = run_test.QUIZE_SCORE
    test_id = run_test.ID_QUIZE
    MAX_QUESTION_SURVEY = await orm.async_get_count_question_test(test_id)
    percent = float(points) / float(MAX_QUESTION_SURVEY) * 100
    percent = round(percent, 2)
    level_id, level_user_text = await orm.async_get_text_level(percent)
    await bot.send_message(chat_id=user_tg_id,
                           text=f'Тест отменен\n'
                                f'Результат: {percent}%\n'
                                f'{points} правильных ответов\n'
                                f'из {MAX_QUESTION_SURVEY} всех вопросов\n'
                                f'Это уровень: {level_user_text}')
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать продолжение теста
async def test_continue(callback: types.CallbackQuery) -> None:
    # user_id = callback.from_user.id
    # test_info = get_user_survey(user_id, 1)[0]
    # user_test_id = test_info[0]
    # set_user_survey_status_test(user_test_id, 4)
    # FSMTest.test_continue.set()
    # ic(await state.get_state())
    await callback.answer('Сейчас можно только остановить тест', show_alert=True)


async def test_completed(callback: types.CallbackQuery, callback_data: ViewResultTestCal) -> None:
    user_tg_id = callback.from_user.id
    user_tset_id = int(callback_data.id_user_test)
    run_test = await orm.async_get_user_test_by_id(user_tset_id)
    await orm.async_set_user_test_status(user_tset_id, 5)

    points = run_test.QUIZE_SCORE
    test_id = run_test.ID_QUIZE
    MAX_QUESTION_SURVEY = await orm.async_get_count_question_test(test_id)
    percent = float(points)/float(MAX_QUESTION_SURVEY) * 100
    percent = round(percent, 2)
    level_id, level_user_text = await orm.async_get_text_level(percent)
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=f'Тест закончен\n'
                                f'Результат: {percent}%\n'
                                f'{points} правильных ответов\n'
                                f'из {MAX_QUESTION_SURVEY} всех вопросов\n'
                                f'Это уровень: {level_user_text}')
    if test_id == 1:
        await orm.async_set_user_level(user_tg_id, level_id)
    await callback.answer()


# TODO Sql+Test -> TODO Sql+Test 1. Реализовать перезапуск теста
async def test_restart(callback: types.CallbackQuery) -> None:
    await callback.answer('Сейчас можно только остановить тест', show_alert=True)


def register_call_handlers_user(router: Router) -> None:
    router.callback_query.register(delete_message, DelMessageCal.filter())
    router.callback_query.register(test_handler, SelectTestCal.filter())
    # dp.register_callback_query_handler(test_run, our_call_datas.run_test.filter())
    router.callback_query.register(test_progress, ProgressTestCal.filter())
    router.callback_query.register(test_completed, ViewResultTestCal.filter())
    # dp.register_callback_query_handler(test_continue, our_call_datas.continue_test.filter())
    router.callback_query.register(test_canceled, CanceledTestCal.filter())
    # dp.register_callback_query_handler(test_restart, our_call_datas.restart_test.filter())
    # dp.register_callback_query_handler(test_stopped, our_call_datas.stop_test.filter())

