from aiogram import types, Dispatcher, filters
from Create_bot import bot, MY_ID
from Keyboards import KB_Reply


async def send_welcome(message: types.Message):
    try:
        await bot.send_message(chat_id=message.chat.id,
                               text=
""" Привет, это бот который проверит твои знания по английскому языку, а в будущем еще и научит.\n
Используй кнопку помощи, если хочешь узнать что может бот сейчас.\n
Или переходи сразу к тесту и удивись своему уровню!""",
                               reply_markup=KB_Reply.set_but_start())
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await message.answer(text="Что-то пошло не так, попробуй ещё раз.")


async def select_test(message: types.Message):
    try:
        await bot.send_message(chat_id=message.chat.id,
                               text='Выберите тест',
                               reply_markup=KB_Reply.set_IKB_select_survey())
        # print('end select test in message handler')
    except Exception as error_exeption:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error_exeption}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


async def help_command(message: types.Message):
    try:
        await bot.send_message(chat_id=message.chat.id,
                               text=
"""
Этот бот умеет переводить словосочетания в инлайн режиме 
если упомянуть @English_Lisa_Bot в сообщениях.
А так же запускать тесты.
В скором времени будет напоминать о тех словах что нужно выучить
""",
                               reply_markup=None)
    except Exception as error_exeption:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error_exeption}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_welcome, filters.Text(equals="START", ignore_case=True))
    dp.register_message_handler(select_test, filters.Text(equals="Пройти тест"))
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(help_command, filters.Text(equals="Помощь"))
