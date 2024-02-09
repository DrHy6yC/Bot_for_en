from typing import Type

from icecream import ic
from sqlalchemy import Engine, select
from sqlalchemy.ext.asyncio import AsyncEngine

from config import session_sql_connect, async_session_sql_connect
from models import Base, UsersORM, QuizzesORM


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


async def async_select_from_db(class_orm: Type[UsersORM] | Type[QuizzesORM]) -> list[Type[UsersORM] | Type[QuizzesORM]]:
    async with async_session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = await session_sql.execute(query)
        result_select = result_execute.scalars().all()
        ic(result_select)
        return result_select


async def async_update_object(object_orm, new_user_param: str) -> None:
    async with async_session_sql_connect() as session_sql:
        object_orm = await session_sql.get(object_orm.__class__, object_orm.ID)
        object_orm.USER_LOGIN = new_user_param
        await session_sql.commit()
