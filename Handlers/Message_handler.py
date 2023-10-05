from aiogram import types, Dispatcher, filters
from aiogram.dispatcher import FSMContext

from Create_bot import bot, MY_ID
from Keyboards import KB_Reply
from FSMStates.FSMTests import FSMTest
# from aiogram.dispatcher import FSMContext


# TODO сделать так, что бы заменялась клавиатура когда вызов из команды
async def send_welcome(message: types.Message):
    try:
        await message.delete()
        reply_markup = KB_Reply.set_IKB_one_but('Ok', 'delete_message')
        if message.text == '/start':
            reply_markup = KB_Reply.set_but_start()

        await bot.send_message(chat_id=message.chat.id,
                               text="""
Привет, это бот который проверит твои знания по английскому языку,\n
а в будущем еще и научит.\n
Используй кнопку помощи, если хочешь узнать что может бот сейчас.\n
Или переходи сразу к тесту и удивись своему уровню!
""",
                               reply_markup=reply_markup)
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await message.answer(text="Что-то пошло не так, попробуй ещё раз.")


async def select_test(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(chat_id=message.chat.id,
                               text='Выберите тест',
                               reply_markup=KB_Reply.set_IKB_select_survey())
        # print('end select test in message handler')
        async with state.proxy() as data:
            data['id_user'] = message.from_user.id
        await FSMTest.test_handler.set()

    except Exception as error_exeption:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error_exeption}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


async def help_command(message: types.Message):
    try:
        await message.delete()
        await bot.send_message(chat_id=message.chat.id,
                               text=
"""
Этот бот умеет переводить словосочетания в инлайн режиме 
если упомянуть @English_Lisa_Bot в сообщениях.
А так же запускать тесты.
В скором времени будет напоминать о тех словах что нужно выучить
""",
                               reply_markup=KB_Reply.set_IKB_one_but('Ok', 'delete_message'))
    except Exception as error_exeption:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error_exeption}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


def register_handlers_user(dp: Dispatcher):

    dp.register_message_handler(send_welcome, commands=['start'], state="*")
    dp.register_message_handler(send_welcome, filters.Text(equals="START", ignore_case=True), state="*")
    dp.register_message_handler(select_test, filters.Text(equals="Пройти тест"))
    dp.register_message_handler(help_command, commands=['help'], state="*")
    dp.register_message_handler(help_command, filters.Text(equals="Помощь"), state="*")
