from aiogram import types, Dispatcher, filters
from aiogram.dispatcher.filters import ChatTypeFilter, IDFilter
from aiogram.types import ContentType, BotCommand
from icecream import ic

from Create_bot import bot, dp
from Keyboards.KB_Reply import set_but_start, set_IKB_one_but, set_IKB_select_survey, set_IKB_grammar_test
from SQL.models import UsersORM
from SQL import orm
from Callback_datas.our_call_datas import del_message


async def delete_message(message: types.Message) -> None:
    ic('Message delete')
    await bot.delete_message(message.chat.id, message.message_id)


async def send_welcome(message: types.Message) -> None:
    await message.delete()
    await set_my_keyboard()
    user_tg_id = message.from_user.id
    user_full_name = f'{message.from_user.full_name}'
    username = message.from_user.username
    reply_markup_start = set_but_start()
    call_data = del_message.new()
    reply_markup_delete = set_IKB_one_but('Ok', call_data)
    TEXT_HI_template = await orm.async_get_const('TEXT_HI')
    TEXT_HI = TEXT_HI_template.CONSTANT_VALUE.replace('@FIO', user_full_name)
    IS_USER = await orm.async_is_user_in_bd(user_tg_id)
    ic(IS_USER)
    if IS_USER:
        await bot.send_message(chat_id=user_tg_id,
                               text=TEXT_HI,
                               reply_markup=reply_markup_delete)
    else:
        message_id = await bot.send_message(chat_id=user_tg_id,
                                            text=TEXT_HI,
                                            reply_markup=reply_markup_start)
        ic(message_id)
        new_user = UsersORM(
            USER_TG_ID=user_tg_id,
            USER_LOGIN=user_full_name,
            USER_FULL_NAME=username
        )
        await orm.async_insert_data_list_to_bd([new_user])


async def stop_bot(message: types.Message):
    dp.stop_polling()
    await dp.wait_closed()
    await bot.close()
    ic(f'{message.from_user.id} остановил бота')


async def select_test(message: types.Message) -> None:
    await delete_message(message)
    name_tests = await orm.async_get_name_test()
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите тест',
                           reply_markup=set_IKB_select_survey(name_tests))


async def help_command(message: types.Message) -> None:
    await message.delete()
    help_txt_temp = await orm.async_get_const('TEXT_HELP')
    TEXT_HELP = help_txt_temp.CONSTANT_VALUE
    call_data = del_message.new()
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
    my_command = [
        BotCommand(command='start',
                   description='Кнопка для внесения пользователя в БД'),
        BotCommand(command='stop',
                   description='Кнопка для остановки бота'),
        BotCommand(command='get_keyboard',
                   description='Кнопка для получения индивидуальной клавиатуры')
    ]
    await bot.set_my_commands(commands=my_command)


async def my_keyboard(message: types.Message) -> None:
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вот персональная клавиатура',
                           reply_markup=set_but_start())


async def get_level_English(message: types.Message) -> None:
    user_tg_id = message.from_user.id
    await bot.delete_message(chat_id=user_tg_id,
                             message_id=message.message_id)
    user_level = await orm.async_get_level_user_text(user_tg_id)
    reply_markup = None
    if user_level != "No level":
        text = f'Твой уровень: {user_level}\n' \
               f'Если хочешь повысить уровень,\n' \
               f' пройди еще раз:\n' \
               f'English Level test. Grammar.'
    else:
        text = f'Твой уровень еще не определен, пройди для начала тест: English Level test. Grammar'
        reply_markup = set_IKB_grammar_test()
    await bot.send_message(chat_id=user_tg_id,
                           text=text,
                           reply_markup=reply_markup)


def register_handlers_user(dispatch: Dispatcher) -> None:
    dispatch.register_message_handler(send_welcome, commands=['start'])
    dispatch.register_message_handler(get_level_English, filters.Text(equals="Узнать уровень"))
    dispatch.register_message_handler(
        select_test,
        filters.Text(equals="Пройти тест"),
        ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
    dispatch.register_message_handler(help_command, commands=['help'])
    dispatch.register_message_handler(help_command, filters.Text(equals="Помощь"))
    dispatch.register_message_handler(
        test_filter_handler,
        ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),
        content_types=ContentType.STICKER)
    dispatch.register_message_handler(my_keyboard, commands=['get_keyboard'])
    dispatch.register_message_handler(stop_bot, IDFilter(chat_id='809916411'), commands=['stop'])
