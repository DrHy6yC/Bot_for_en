from aiogram import types, Dispatcher

from magic_filter import F
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot
from Keyboards import KB_Reply
from Utils.From_DB import get_id_survey, get_answer, get_question, get_one_answer, get_count_question


async def delete_message(callback: types.CallbackQuery) -> None:
    print('Message delete')
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    return await callback.answer()


async def test_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO 5 Отправить в БД ид теста
    print(await state.get_state() == 'FSMTest:test_handler')
    name_test = callback.data.replace("Run test: ", "")
    id_test = get_id_survey(name_test)
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


# TODO 1 получать из бд информацию о пользователе и тесте
async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    id_chat = callback.message.chat.id
    data = await state.get_data()
    test_id = data['id_test']
    MAX_QUESTION_SURVEY = get_count_question(int(test_id))
    question_num = data.get('question_num', 0)
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
        # TODO TEST !!! не работает без проверки если сообщение не было изменено.
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


# TODO 6 Реализация расчета результата
async def test_canceled(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест Прерван\nРезультат - хз')
    await callback.answer()


# TODO 2 Реализовать после внедрения сохранения в бд по TODO 1
async def test_continue(callback: types.CallbackQuery, state: FSMContext) -> None:
    pass


async def test_completed(callback: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await state.finish()
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест закончен\nРезультат - хз')
    await callback.answer()


# TODO 3 Реализовать перезапуск теста, нужен TODO 1
async def test_restart(callback: types.CallbackQuery, state: FSMContext) -> None:
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
