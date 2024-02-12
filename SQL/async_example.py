from icecream import ic
import asyncio

from SQL.create_min_in_DB import filling_min_db
from config import sql_async_engine

from models import UsersORM, QuizzesORM, ConstantsORM, QuizeStatusesORM
from orm import async_create_all_table, async_insert_data_list_to_bd, async_select_from_db, \
    async_get_const, async_select_user_by_id, async_is_user_in_bd, async_get_name_survey_for_ikb, \
    async_get_is_user_status_test


async def rewrite_DB():
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
    hi_txt = """   Привет, @FIO! Это бот который проверит твои знания по английскому языку,а в будущем еще и научит.
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

    status_quize_Selected = QuizeStatusesORM(
        ID=1,
        STATUS_TEXT='Selected'
    )

    status_quize_Launched = QuizeStatusesORM(
        ID=2,
        STATUS_TEXT='Launched'
    )
    status_quize_Stopped = QuizeStatusesORM(
        ID=3,
        STATUS_TEXT='Stopped'
    )
    status_quize_Revoked = QuizeStatusesORM(
        ID=4,
        STATUS_TEXT='Revoked'
    )
    status_quize_Completed = QuizeStatusesORM(
        ID=5,
        STATUS_TEXT='Completed'
    )

    status_quize_Deleted = QuizeStatusesORM(
        ID=6,
        STATUS_TEXT='Deleted'
    )

    await async_create_all_table(sql_async_engine)
    await async_insert_data_list_to_bd([user_di, user_admin, mini_test, grammar_level_test, TEXT_HI, TEXT_HELP,
                                        status_quize_Selected, status_quize_Launched,status_quize_Stopped,
                                        status_quize_Revoked, status_quize_Completed, status_quize_Deleted])


async def check_db():
    users = await async_select_from_db(UsersORM)
    quizzes = await async_select_from_db(QuizzesORM)
    consts = await async_select_from_db(ConstantsORM)
    for user in users:
        ic(user.USER_LOGIN)
    for quize in quizzes:
        ic(quize.QUIZE_NAME)
    for const in consts:
        ic(const.CONSTANT_NAME)


async def tasks():
    await filling_min_db()
    # await async_get_is_user_status_test(3242342, 1)

if __name__ == "__main__":
    # asyncio.run(rewrite_DB())
    # asyncio.run(check_db())
    asyncio.run(tasks())
