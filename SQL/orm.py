from typing import Type, Union

from icecream import ic
from sqlalchemy import Engine, select
from sqlalchemy.ext.asyncio import AsyncEngine

from SQL.config import session_sql_connect, async_session_sql_connect
from SQL.models import Base, UsersORM, QuizzesORM, ConstantsORM

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
    dictionary = dict()
    list_tests = await async_select_from_db(QuizzesORM)
    for test in list_tests:
        name_test = test.QUIZE_NAME
        dictionary[name_test] = f'Run test: {name_test}'
    dictionary['Отмена'] = f'delete_message'
    return dictionary


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
