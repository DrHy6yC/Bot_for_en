from icecream import ic

from sqlalchemy import MetaData, Table, Column, Integer, BigInteger, String, select, insert, text

from sqlalchemy.engine.base import Engine
# Альтернатива orm


# Функции
def select_table_from_db(engine: Engine, table: Table) -> None:
    with engine.connect() as session:
        sql_query = select(table)
        res_query = session.execute(sql_query)
        result = res_query.all()
        ic(result)


def insert_to_db(engine: Engine, user_table: Table, values_list_dict: list) -> None:
    with engine.connect() as session:
        sql_query = insert(user_table).values(values_list_dict)
        session.execute(sql_query)
        session.commit()


def create_all_table(metadata: MetaData, engine: Engine) -> None:
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


def execute_any_query(engine: Engine, query: str) -> None:
    """
    Функция для выполнения набора sql-команд на базе с комитом

    NOTE:
        При смене диалекта SQL нужно учитывать что конкретный запрос не  обработанный sqlalshemy
        могут не выполняться на других БД

    :param engine: принимает sql_engine/подключение
    :param query: принимает sql-выражение в виде текста
    :return: ничего не возвращает
    """
    with engine.connect() as session:
        session.execute(text(query))
        session.commit()


# Модели
meta_data = MetaData()

users_table = Table(
    "USERS",
    meta_data,
    Column("ID", Integer, primary_key=True),
    Column("USER_TG_ID", BigInteger),
    Column("USER_FULL_NAME", String(250)),
    Column("USER_LEVEL", Integer, default=0),
    Column("USER_ACCESS", Integer, default=0),
    Column("USER_LOGIN", String(50))
)


quizzes_table = Table(
    "QUIZZES",
    meta_data,
    Column("ID", Integer, primary_key=True),
    Column("QUIZE_NAME", String(250)),
    Column("QUIZE_DESCRIPTION", String(500))
)


TRIGGER_USERS_AFTER_UPDATE = """
    CREATE DEFINER = CURRENT_USER TRIGGER Example.USERS_AFTER_UPDATE BEFORE UPDATE
    ON USERS FOR EACH ROW
    BEGIN
        SET NEW.USER_UPDATE_TIME = current_timestamp();
    END
    """
