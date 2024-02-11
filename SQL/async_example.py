from icecream import ic
import asyncio

from config import sql_async_engine

from models import UsersORM, QuizzesORM, ConstantsORM
from orm import async_create_all_table, async_insert_data_list_to_bd, async_select_from_db, \
    async_get_const, async_select_user_by_id, async_is_user_in_bd, async_get_name_survey_for_ikb


async def tasks():
    user_di = UsersORM(
        USER_TG_ID=23423,
        USER_LOGIN='DI_hy6',
        USER_FULL_NAME='Di Cho Nah'
    )
    user_admin = UsersORM(
        USER_TG_ID=2342254345,
        USER_LOGIN='Admin',
        USER_FULL_NAME='Admin Bot'
    )
    grammar_level_test = QuizzesORM(
        QUIZE_NAME='English Level test. Grammar',
        QUIZE_DESCRIPTION='Тест для проверки уровня грамматики по английскому'
    )

    mini_test = QuizzesORM(
        QUIZE_NAME='Mini text',
        QUIZE_DESCRIPTION='Мини тест для проверки тестов'
    )

    help_txt = """  Этот бот умеет переводить словосочетания в инлайн режиме
    если упомянуть @English_bot_help_HW_bot в сообщениях.
    Ещё запускать тесты. В скором времени будет напоминать о тех словах что нужно выучить.
        """
    hi_txt = """    Привет, @FIO! Это бот который проверит твои знания по английскому языку,а в будущем еще и научит.
    Используй кнопку помощи, если хочешь узнать что может бот сейчас.
    Или переходи сразу к тесту и удивись своему уровню!"""

    TEXT_HI = ConstantsORM(
        CONSTANT_NAME='TEXT_HI',
        CONSTANT_VALUE=hi_txt
    )

    TEXT_HELP = ConstantsORM(
        CONSTANT_NAME='TEXT_HELP',
        CONSTANT_VALUE=help_txt
    )

    await async_insert_data_list_to_bd([user_di, user_admin, mini_test, grammar_level_test, TEXT_HI, TEXT_HELP])
    await async_create_all_table(sql_async_engine)


async def tasks1():
    users = await async_select_from_db(UsersORM)
    quizzes = await async_select_from_db(QuizzesORM)
    consts = await async_select_from_db(ConstantsORM)
    for user in users:
        ic(user.USER_LOGIN)
    for quize in quizzes:
        ic(quize.QUIZE_NAME)
    for const in consts:
        ic(const.CONSTANT_NAME)


async def tasks2():
    await async_get_name_survey_for_ikb()

if __name__ == "__main__":
    # asyncio.run(tasks())
    # asyncio.run(tasks1())
    asyncio.run(tasks2())
