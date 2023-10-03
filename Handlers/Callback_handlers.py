from copy import copy
from aiogram import types, Dispatcher
from Create_bot import bot, MY_ID, sql_bot
from Keyboards import KB_Reply
from FSMStates.FSMTests import FSMTest
from aiogram.dispatcher import FSMContext


async def test_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Отправить в БД ид теста
    try:
        name_test = callback.data.replace("Run test: ", "")
        async with state.proxy() as data:
            data['name_test'] = name_test
            print(data)
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=f'Выбран тест: {name_test}')
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=KB_Reply.set_IKB_run_survey(name_test))
        await FSMTest.test_run.set()
    except Exception as error_exception:
        await bot.send_message(chat_id=MY_ID,
                               text=str(error_exception))


async def test_run(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO получать из бд информацию о пользователе и тесте
    try:
        question = 'First question'
        answers = ['1', '2', '3', '4']

        async with state.proxy() as data:
            data['question_num'] = 1
            print(data)

        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=None
        )
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=question,
                               reply_markup=KB_Reply.set_IKB_Survey(answers))
        await FSMTest.test_progressed.set()

    except Exception as error_exception:
        await bot.send_message(chat_id=MY_ID,
                               text=str(error_exception))


async def test_progress(callback: types.CallbackQuery, state: FSMContext) -> None:
    # TODO получить и отправить из бд
    try:
        print(callback.from_user.id)
        async with state.proxy() as data:
            data['question_num'] += 1
            print(data)
        print('Тест идет')

    except Exception as error_except:
        print('Error in handlers test progress: ', error_except)


async def test_revoked(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    # TODO Добавить возможность продолжить или перезапустить тест
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тест прерван',
                           reply_markup=None)
    await FSMTest.test_revoked.set()


def register_call_handlers_user(dp: Dispatcher) -> None:
    list_surveys = sql_bot.select_column_table('SURVEYS', 'SURVEY_NAME')
    for name_test in list_surveys:
        data = f'Run test: {name_test}'
        print(data)
        dp.register_callback_query_handler(test_handler, text=copy(data), state=FSMTest.test_handler)

    dp.register_callback_query_handler(test_run, state=FSMTest.test_run)
    dp.register_message_handler(test_progress, state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text='1', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text='2', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text='3', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_progress, text='4', state=FSMTest.test_progressed)
    dp.register_callback_query_handler(test_revoked, text='0', state=FSMTest.test_progressed)
