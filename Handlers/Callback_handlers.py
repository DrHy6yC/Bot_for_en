from copy import copy

from aiogram import types, Dispatcher

from magic_filter import F
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext

from Create_bot import bot, MY_ID, sql
from Keyboards import KB_Reply


async def delete_message(callback: types.CallbackQuery) -> None:
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)


async def test_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    # # Отправить в БД ид теста
    name_test = callback.data.replace("Run test: ", "")
    await state.update_data(name_test=name_test)
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        parse_mode="html",
        text=f'Выбран тест: {name_test}')
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=KB_Reply.set_IKB_one_but(f'Запустить {name_test}', '1'))
    await FSMTest.test_run.set()
    await callback.answer()



async def test_run(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO получать из бд информацию о пользователе и тесте
    question = 'Выбрано - ______! Вопрос №'
    answers = ['1', '2', '3', '4']
    question_num = 1
    await FSMTest.test_progressed.set()
    async with state.proxy() as data:
        data['question_num'] = question_num
        data['question'] = question
        print(data)

    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=f'{question} {str(question_num)}',
                           reply_markup=KB_Reply.set_IKB_Survey(answers))
    await callback.answer()

async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    pass
    # # TODO получить и отправить из бд
    # try:
    #     await FSMTest.test_progressed.set()
    #     id_chat = callback.message.chat.id
    #     print(callback.from_user.id)
    #     print('Тест идет')
    #     answers = ['1', '2', '3', '4']
    #     answer_user = str(callback.data)
    #     question = 'Выбрано - ______! Вопрос №'
    #     print(question)
    #     text_q = question.replace('______', f'<u><em>{answer_user}</em></u>')
    #     print(text_q)
    #     await bot.edit_message_reply_markup(
    #         chat_id=id_chat,
    #         message_id=callback.message.message_id,
    #         reply_markup=None)
    #     await bot.edit_message_text(
    #         chat_id=id_chat,
    #         message_id=callback.message.message_id,
    #         parse_mode="html",
    #         text=text_q)
    #     print(answer_user)
    #     if answer_user != '0':
    #         async with state.proxy() as data:
    #             data['question_num'] += 1
    #             question_num = data['question_num']
    #             print(data)
    #         await bot.send_message(chat_id=callback.message.chat.id,
    #                                text=f'{question} {str(question_num)}',
    #                                reply_markup=KB_Reply.set_IKB_Survey(answers))
    #     else:
    #         await FSMTest.test_revoked.set()
    #         print('test revoked')
    #     await callback.answer()
    # except Exception as error_except:
    #     print('Error in handlers test progress: ', error_except)


async def test_revoked(callback: types.CallbackQuery) -> None:
    pass
    # await bot.edit_message_reply_markup(
    #     chat_id=callback.message.chat.id,
    #     message_id=callback.message.message_id,
    #     reply_markup=None
    # )
    # await bot.send_message(chat_id=callback.message.chat.id,
    #                        text='Тест прерван',
    #                        reply_markup=KB_Reply.set_IKB_continue_finish())
    # await callback.answer()


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


async def test_finish(callback:  types.CallbackQuery) -> None:
    pass
    # await bot.edit_message_reply_markup(
    #     chat_id=callback.message.chat.id,
    #     message_id=callback.message.message_id,
    #     reply_markup=None)
    # await FSMTest.next()
    # await callback.answer()
    # await bot.send_message(chat_id=callback.message.chat.id,
    #                        text='Тест закончен\nРезультат - хз')


def register_call_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(test_handler, F.data.startswith('Run test: '), state=FSMTest.test_handler)
    dp.register_callback_query_handler(test_run, state=FSMTest.test_run)
    dp.register_message_handler(test_progress, state=FSMTest.test_progressed)
    # dp.register_callback_query_handler(test_progress, state=FSMTest.test_progressed)
    # dp.register_callback_query_handler(test_revoked, state=FSMTest.test_progressed)
    # dp.register_callback_query_handler(test_continue, state=FSMTest.test_continue)
    dp.register_callback_query_handler(delete_message, state="*", text='delete_message')
