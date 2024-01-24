from aiogram import types, Dispatcher, filters
from aiogram.dispatcher import FSMContext
from FSMStates.FSMTests import FSMTest

from Create_bot import bot
from Keyboards import KB_Reply
from Utils.From_DB import get_const, find_user_bd, insert_user_in_db


# TODO вставить имя в приветствие (проверить на новых пользователях, первое приветствие не должно убираться)
async def send_welcome(message: types.Message):
    user_tg_id = message.from_user.id
    user_full_name = f'{message.from_user.full_name}'
    username = message.from_user.username
    print(user_tg_id, user_full_name, username)
    print(message)
    await message.delete()
    reply_markup = KB_Reply.set_but_start()
    TEXT_HI = get_const('TEXT_HI')
    IS_USER = find_user_bd(user_tg_id)

    if IS_USER:
        # Возможность убирать последующие приветсятвие инлайн кнопкой
        reply_markup = KB_Reply.set_IKB_one_but('Ok', 'delete_message')
    else:
        insert_user_in_db(user_tg_id, user_full_name, username)

    await bot.send_message(chat_id=message.chat.id,
                           text=TEXT_HI,
                           reply_markup=reply_markup)


async def select_test(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text='Выберите тест',
                           reply_markup=KB_Reply.set_IKB_select_survey())
    async with state.proxy() as data:
        data['id_user'] = message.from_user.id
    await FSMTest.test_handler.set()


async def help_command(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id,
                           text=get_const('TEXT_HELP'),
                           reply_markup=KB_Reply.set_IKB_one_but('Ok', 'delete_message'))


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'], state="*")
    dp.register_message_handler(send_welcome, filters.Text(equals="START", ignore_case=True), state="*")
    dp.register_message_handler(select_test, filters.Text(equals="Пройти тест"))
    dp.register_message_handler(help_command, commands=['help'], state="*")
    dp.register_message_handler(help_command, filters.Text(equals="Помощь"), state="*")
