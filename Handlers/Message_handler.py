from aiogram.dispatcher.filters import ChatTypeFilter
from icecream import ic
from aiogram import types, Dispatcher, filters
from FSMStates.FSMTests import FSMTest

from Create_bot import bot
from Keyboards import KB_Reply
from Utils.From_DB import get_const, find_user_bd, insert_user_in_db


async def send_welcome(message: types.Message) -> None:
    await message.delete()
    user_tg_id = message.from_user.id
    user_full_name = f'{message.from_user.full_name}'
    username = message.from_user.username
    reply_markup_start = KB_Reply.set_but_start()
    reply_markup_delete = KB_Reply.set_IKB_one_but('Ok', 'delete_message')
    TEXT_HI = get_const('TEXT_HI').replace('@FIO', user_full_name)
    ic(user_tg_id)
    IS_USER = find_user_bd(user_tg_id)
    ic(IS_USER)
    if IS_USER:
        await bot.send_message(chat_id=user_tg_id,
                               text=TEXT_HI,
                               reply_markup=reply_markup_delete)
    else:
        message_id = await bot.send_message(chat_id=user_tg_id,
                                            text=TEXT_HI,
                                            reply_markup=reply_markup_start)
        insert_user_in_db(user_tg_id, user_full_name, username, message_id.message_id)


async def select_test(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите тест',
                           reply_markup=KB_Reply.set_IKB_select_survey())
    await FSMTest.test_handler.set()


async def help_command(message: types.Message) -> None:
    await message.delete()
    await bot.send_message(chat_id=message.from_user.id,
                           text=get_const('TEXT_HELP'),
                           reply_markup=KB_Reply.set_IKB_one_but('Ok', 'delete_message'))


def register_handlers_user(dp: Dispatcher) -> None:
    dp.register_message_handler(send_welcome, commands=['start'], state="*")
    dp.register_message_handler(send_welcome, filters.Text(equals="START", ignore_case=True), state="*")
    dp.register_message_handler(select_test,
                                filters.Text(equals="Пройти тест"),
                                ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
    dp.register_message_handler(help_command, commands=['help'], state="*")
    dp.register_message_handler(help_command, filters.Text(equals="Помощь"), state="*")
