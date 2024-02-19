from copy import copy

from icecream import ic
from aiogram import types, Router
from aiogram.filters import Command
from aiogram import F

from Create_bot import bot, dp
from Commands import my_command, start_command, help_command, stop_bot_command, get_private_command
from Keyboards import set_buts, set_IKB_one_but, set_IKB_many_but
from SQL.models import UsersORM
from SQL import orm
from Callback_datas.our_call_datas import DelMessageCal, SelectTestCal, del_message


async def delete_message(message: types.Message) -> None:
    ic('Message delete')
    await bot.delete_message(message.chat.id, message.message_id)


async def send_welcome(message: types.Message) -> None:
    user_tg_id = message.from_user.id
    await message.delete()
    await set_my_keyboard()
    user_full_name = f'{message.from_user.full_name}'
    username = message.from_user.username
    text_buts = ['Помощь', 'Пройти тест', 'Узнать уровень']
    TEXT_HI_template = await orm.async_get_const('TEXT_HI')
    TEXT_HI = TEXT_HI_template.CONSTANT_VALUE.replace('@FIO', user_full_name)
    IS_USER = await orm.async_is_user_in_bd(user_tg_id)
    ic(IS_USER)
    if IS_USER:
        await bot.send_message(chat_id=user_tg_id,
                               text=TEXT_HI,
                               reply_markup=set_IKB_one_but('Ok', DelMessageCal()))
    else:
        message_id = await bot.send_message(chat_id=user_tg_id,
                                            text=TEXT_HI,
                                            reply_markup=set_buts(text_buts))
        ic(message_id)
        new_user = UsersORM(
            USER_TG_ID=user_tg_id,
            USER_LOGIN=user_full_name,
            USER_FULL_NAME=username
        )
        await orm.async_insert_data_list_to_bd([new_user])


async def stop_bot(message: types.Message):
    user_tg_id = copy(message.from_user.id)
    await dp.stop_polling()
    ic(f'{user_tg_id} остановил бота')
    await bot.close()


async def select_test(message: types.Message) -> None:
    await delete_message(message)
    name_tests = await orm.async_get_name_test()
    dict_buts = dict()
    for name_test in name_tests:
        dict_buts[name_test] = SelectTestCal(name_test=name_test)
    dict_buts['Отмена'] = DelMessageCal()
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите тест',
                           reply_markup=set_IKB_many_but(dict_buts))


async def help_func(message: types.Message) -> None:
    await message.delete()
    help_txt_temp = await orm.async_get_const('TEXT_HELP')
    TEXT_HELP = help_txt_temp.CONSTANT_VALUE
    call_data = del_message
    await bot.send_message(chat_id=message.from_user.id,
                           text=TEXT_HELP,
                           reply_markup=set_IKB_one_but('Ok', call_data))


async def test_filter_handler(message: types.Message) -> None:
    ic(message)
    id_user = message.from_user.id
    id_chat = message.chat.id
    id_message = message.message_id

    await bot.delete_message(chat_id=id_chat,
                             message_id=id_message)
    await bot.send_message(chat_id=id_user,
                           text='Не шли стикеры иначе засру личку')
    await bot.send_sticker(chat_id=id_user,
                           sticker='CAACAgIAAx0CbjGesQACAaNlu9Nn_55FcbPgKHv2fy6bTyEk6QACRRUAAm7NwEql3a6mlLHZ6DQE')


async def set_my_keyboard() -> None:
    await bot.set_my_commands(commands=my_command)


async def my_keyboard(message: types.Message) -> None:
    text_buts = ['Помощь', 'Пройти тест', 'Узнать уровень']
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вот персональная клавиатура',
                           reply_markup=set_buts(text_buts))


async def get_level_English(message: types.Message) -> None:
    user_tg_id = message.from_user.id
    await bot.delete_message(chat_id=user_tg_id,
                             message_id=message.message_id)
    user_level = await orm.async_get_level_user_text(user_tg_id)
    if user_level != "No level":
        text = f'Твой уровень: {user_level}\n' \
               f'Если хочешь повысить уровень,\n' \
               f' пройди еще раз:\n' \
               f'English Level test. Grammar.'
    else:
        text = f'Твой уровень еще не определен, пройди для начала тест: English Level test. Grammar'
        name_test = 'English Level test. Grammar'
        dict_buts = dict()
        call_data_1 = SelectTestCal(name_test=name_test)
        call_data_2 = DelMessageCal()
        dict_buts[name_test] = call_data_1
        dict_buts['Отмена'] = call_data_2
    await bot.send_message(chat_id=user_tg_id,
                           text=text,
                           reply_markup=set_IKB_many_but(dict_buts))


def register_handlers_message(router: Router) -> None:
    router.message.register(send_welcome, Command(start_command))
    router.message.register(get_level_English, (F.text == "Узнать уровень"))
    router.message.register(
        select_test,
        (F.text == "Пройти тест")
        # ChatTypeFilter(chat_type=types.ChatType.PRIVATE)
    )
    router.message.register(help_func, Command(help_command))
    router.message.register(help_func, (F.text == "Помощь"))
    router.message.register(
        test_filter_handler,
        # ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),
        F.content_type.in_({'sticker'})
    )
    router.message.register(my_keyboard, Command(get_private_command))
    router.message.register(stop_bot, F.from_user.id.in_({809916411}), Command(stop_bot_command))
