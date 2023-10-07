from aiogram import types, Dispatcher, filters
from aiogram.dispatcher import FSMContext
from FSMStates.FSMTests import FSMTest

from Create_bot import bot, sql
from Keyboards import KB_Reply
from Utils import SQL_querys as query


async def send_welcome(message: types.Message):
    await message.delete()
    reply_markup = KB_Reply.set_IKB_one_but('Ok', 'delete_message')
    if message.text == '/start':
        reply_markup = KB_Reply.set_but_start()

    await bot.send_message(chat_id=message.chat.id,
                           text=sql.select_db_one(
                               query=query.select_all_from_CONSTANTS_by_CONSTANT_NAMES,
                               data={'CONSTANT_NAMES': 'TEXT_HI'})[0],
                           reply_markup=reply_markup)


async def select_test(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Выберите тест',
                           reply_markup=KB_Reply.set_IKB_select_survey())
    # print('end select test in message handler')
    async with state.proxy() as data:
        data['id_user'] = message.from_user.id
    await FSMTest.test_handler.set()


async def help_command(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text=sql.select_db_one(query=query.select_all_from_CONSTANTS_by_CONSTANT_NAMES,
                                                  data={'CONSTANT_NAMES': 'TEXT_HELP'})[0],
                           reply_markup=KB_Reply.set_IKB_one_but('Ok', 'delete_message'))


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'], state="*")
    dp.register_message_handler(send_welcome, filters.Text(equals="START", ignore_case=True), state="*")
    dp.register_message_handler(select_test, filters.Text(equals="Пройти тест"))
    dp.register_message_handler(help_command, commands=['help'], state="*")
    dp.register_message_handler(help_command, filters.Text(equals="Помощь"), state="*")
