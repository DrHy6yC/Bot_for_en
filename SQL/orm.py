from typing import Type, Union

from icecream import ic
from sqlalchemy import Engine, select, func, and_, desc
from sqlalchemy.ext.asyncio import AsyncEngine

from SQL.config import session_sql_connect, async_session_sql_connect
from SQL.models import Base, UsersORM, QuizzesORM, ConstantsORM, UserQuizzesORM

ModelsORM = UsersORM, QuizzesORM, ConstantsORM


# Example:
# ================================async===================================
async def async_create_all_table(async_engine: AsyncEngine) -> None:
    """
    Пересоздает(Если есть) все таблицы наследуемые от Base
    :param async_engine: Принимает sql_async_engine/подключение
    :return: Ничего не возвращает
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_insert_data_list_to_bd(list_data: list) -> None:
    async with async_session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        await session_sql.commit()


async def async_select_from_db(class_orm: Union[ModelsORM]) -> list[Union[ModelsORM]]:
    async with async_session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().all()
        ic(result)
        return result


async def async_update_object(object_orm, new_user_param: str) -> None:
    async with async_session_sql_connect() as session_sql:
        object_orm = await session_sql.get(object_orm.__class__, object_orm.ID)
        object_orm.USER_LOGIN = new_user_param
        await session_sql.commit()


async def async_get_const(name_const: str) -> ConstantsORM:
    async with async_session_sql_connect() as session_sql:
        query = select(ConstantsORM).where(ConstantsORM.CONSTANT_NAME == name_const)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one()
        return result


async def async_select_user_by_id(user_tg_id: int) -> UsersORM:
    async with async_session_sql_connect() as session_sql:
        query = select(UsersORM).where(UsersORM.USER_TG_ID == user_tg_id)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one()
        ic(result)
        return result


async def async_is_user_in_bd(user_tg_id: int) -> bool:
    async with async_session_sql_connect() as session_sql:
        query = select(UsersORM).where(UsersORM.USER_TG_ID == user_tg_id)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one_or_none()
        if result:
            return True
        else:
            return False


async def async_get_name_survey_for_ikb() -> dict[str, str]:
    ic('ЗАМЕНИТЬ!! должно выводить dict[str, CallbackData]')
    dictionary = dict()
    list_tests = await async_select_from_db(QuizzesORM)
    for test in list_tests:
        name_test = test.QUIZE_NAME
        dictionary[name_test] = f'Run test: {name_test}'
    dictionary['Отмена'] = f'delete_message'
    return dictionary


async def async_get_is_user_status_test(user_id, status) -> bool:
    async with async_session_sql_connect() as session_sql:
        query = select(func.count(UserQuizzesORM.ID)).\
            select_from(UserQuizzesORM).\
            where(and_(UserQuizzesORM.ID_USER_TG == user_id, UserQuizzesORM.QUIZE_STATUS == status))
        user_exec = await session_sql.execute(query)
        user = user_exec.scalars().one_or_none()
    is_user_status_test: bool = user != 0
    ic(user)
    ic(is_user_status_test)
    return is_user_status_test


async def async_get_user_survey(user_id, status) -> UserQuizzesORM:
    async with async_session_sql_connect() as session_sql:
        query = select(UserQuizzesORM).\
            select_from(UserQuizzesORM).\
            where(and_(UserQuizzesORM.ID_USER == user_id, UserQuizzesORM.QUIZE_STATUS == status)).\
            order_by(desc(UserQuizzesORM.CREATE_TIME))
        users_exec = await session_sql.execute(query)
        user = users_exec.scalars().first()
        return user


async def async_get_id_test(name_test: str) -> int:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM.ID).\
            select_from(QuizzesORM).\
            where(QuizzesORM.QUIZE_NAME == name_test)
        tests_exec = await session_sql.execute(query)
        test = tests_exec.scalars().first()
        return test


async def async_set_user_test_status(user_test_id: int, status: int) -> None:
    async with async_session_sql_connect() as session_sql:
        user_test = session_sql.get(UserQuizzesORM, user_test_id)
        user_test.QUIZE_STATUS = status
        await session_sql.commit()


# =====================sync===================
def create_all_table(engine: Engine) -> None:
    """
    Пересоздает(Если есть) все таблицы наследуемые от Base
    :param engine: Принимает sql_engine/подключение
    :return: Ничего не возвращает
    """
    ic(Base.registry.metadata.tables)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_data_list_to_bd(list_data: list) -> None:
    with session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        session_sql.commit()


def select_from_db(class_orm: Type[UsersORM] | Type[QuizzesORM]) -> list:
    with session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = session_sql.execute(query)
        result_select = result_execute.scalars().all()
        ic(result_select)
        return result_select


def update_object(object_orm, new_user_param: str) -> None:
    with session_sql_connect() as session_sql:
        object_orm = session_sql.get(object_orm.__class__, object_orm.ID)
        object_orm.USER_LOGIN = new_user_param
        session_sql.commit()
