from icecream import ic
import asyncio

from config import db_mysql, sql_async_engine

from models import UsersORM, QuizzesORM
from orm import async_create_all_table, async_insert_data_list_to_bd, async_select_from_db, async_update_object


async def tasks():
    user_di = UsersORM(
        USER_TG_ID=2312142232,
        USER_LOGIN='DI_hy6',
        USER_FULL_NAME='Di Cho Nah'
    )
    grammar_level_test = QuizzesORM(
        QUIZE_NAME='English Level test. Grammar',
        QUIZE_DESCRIPTION='Тест для проверки уровня грамматики по английскому'
    )
    if db_mysql.get_db_is_created():
        await async_create_all_table(sql_async_engine)
        # Не работает на sqlite
        # execute_any_query(sql_engine, TRIGGER_USERS_AFTER_UPDATE)
    await async_insert_data_list_to_bd([user_di, grammar_level_test])
    users = await async_select_from_db(UsersORM)
    user_di = users[0]
    await async_select_from_db(QuizzesORM)
    await async_update_object(user_di, '93_Di~ME4EHbIN`_23RUS')
    users = await async_select_from_db(UsersORM)
    user_di = users[0]
    ic(user_di.USER_LOGIN)


if __name__ == "__main__":
    asyncio.run(tasks())
