from aiogram import types, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import ContentType
from aiogram.utils.keyboard import InlineKeyboardBuilder
from icecream import ic
from aiogram import F

from Create_bot import bot, dp
from Commands import my_command, start_command, help_command, stop_bot_command, get_private_command
from Keyboards.KB_Reply import set_but_start, set_IKB_one_but #, set_IKB_select_survey, set_IKB_grammar_test
from SQL.models import UsersORM
from SQL import orm
from Callback_datas.our_call_datas import DelMessageCal, SelectTestCal


# async def delete_message(message: types.Message) -> None:
#     ic('Message delete')
#     await bot.delete_message(message.chat.id, message.message_id)


async def send_welcome(message: types.Message) -> None:
    user_tg_id = message.from_user.id
    await message.delete()
    await set_my_keyboard()
    # DelMessageCal()
    # reply_markup_delete = set_IKB_one_but('Ok', call_data)
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Ok',
        callback_data=DelMessageCal(),
    )
    await bot.send_message(
        chat_id=user_tg_id,
        text=f"What do you want to do?",
        reply_markup=builder.as_markup(),
    )

    # user_full_name = f'{message.from_user.full_name}'
    # username = message.from_user.username
    # reply_markup_start = set_but_start()
    # call_data = CallbackData()   #del_message.new()
    # reply_markup_delete = set_IKB_one_but('Ok', call_data)
    # TEXT_HI_template = await orm.async_get_const('TEXT_HI')
    # TEXT_HI = TEXT_HI_template.CONSTANT_VALUE.replace('@FIO', user_full_name)
    # IS_USER = await orm.async_is_user_in_bd(user_tg_id)
    # ic(IS_USER)
    # if IS_USER:
    #     await bot.send_message(chat_id=user_tg_id,
    #                            text=TEXT_HI,
    #                            reply_markup=reply_markup_delete)
    # else:
    #     message_id = await bot.send_message(chat_id=user_tg_id,
    #                                         text=TEXT_HI,
    #                                         reply_markup=reply_markup_start)
    #     ic(message_id)
    #     new_user = UsersORM(
    #         USER_TG_ID=user_tg_id,
    #         USER_LOGIN=user_full_name,
    #         USER_FULL_NAME=username
    #     )
    #     await orm.async_insert_data_list_to_bd([new_user])


async def stop_bot(message: types.Message):
    dp.stop_polling()
    await dp.wait_closed()
    await bot.close()
    ic(f'{message.from_user.id} остановил бота')


async def select_test(message: types.Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text='Не шли стикеры иначе засру личку')
#     await delete_message(message)
#     name_tests = await orm.async_get_name_test()
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Выберите тест',
#                            reply_markup=set_IKB_select_survey(name_tests))


async def help_func(message: types.Message) -> None:
    await message.delete()
    help_txt_temp = await orm.async_get_const('TEXT_HELP')
    TEXT_HELP = help_txt_temp.CONSTANT_VALUE
    call_data = DelMessageCal
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
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вот персональная клавиатура',
                           reply_markup=set_but_start())


async def get_level_English(message: types.Message) -> None:
    await message.answer("You levels")
#     user_tg_id = message.from_user.id
#     await bot.delete_message(chat_id=user_tg_id,
#                              message_id=message.message_id)
#     user_level = await orm.async_get_level_user_text(user_tg_id)
#     reply_markup = None
#     if user_level != "No level":
#         text = f'Твой уровень: {user_level}\n' \
#                f'Если хочешь повысить уровень,\n' \
#                f' пройди еще раз:\n' \
#                f'English Level test. Grammar.'
#     else:
#         text = f'Твой уровень еще не определен, пройди для начала тест: English Level test. Grammar'
#         reply_markup = set_IKB_grammar_test()
#     await bot.send_message(chat_id=user_tg_id,
#                            text=text,
#                            reply_markup=reply_markup)


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
        # content_types=ContentType.STICKER
    )
    router.message.register(my_keyboard, Command(get_private_command))
    router.message.register(stop_bot, F.from_user.id.in_({809916411}), Command(stop_bot_command))
