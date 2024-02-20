from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.asyncio import create_async_engine


def get_engine(dsn_db: str, is_echo: bool) -> Engine:
    """
    Функция запуска главного движка sql/подключения синхронно

    :return: возвращает экземпляр класса Engine из sqlalchemy.engine.base

    Parameters:
    -----------

    dsn_db: принимает в себя строку подключения
    is_echo: включения/отключения транслирования команд SQL генерируемых sqlalchemy в консоль

    """
    engine = create_engine(
        url=dsn_db,
        echo=is_echo
    )
    return engine


def get_async_engine(async_dsn_db: str, is_echo: bool) -> Engine:
    """
    Функция запуска главного движка sql/подключения синхронно
    :dsn_db: принимает в себя строку подключения
    :is_echo: включения/отключения транслирования команд SQL генерируемых sqlalchemy в консоль
    :return: возвращает экземпляр класса Engine из sqlalchemy.engine.base
    """
    engine = create_async_engine(
        url=async_dsn_db,
        echo=is_echo

    )
    return engine

