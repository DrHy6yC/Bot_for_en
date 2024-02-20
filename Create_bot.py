from os import getenv
from dotenv import load_dotenv

from icecream import ic

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import async_sessionmaker

from SQL.Engine import get_async_engine
from SQL.Database import DBMYSQL
from Utils import get_bool_from_str

# TODO Bot. Проработать обычные кнопки для лички и для группы
# TODO Bot. Реализовать запуск теста только в личку, если запускался в группе результат отправлялся еще и в группу
# TODO Bot+Sql. Разграничить пользователей по ролям
# TODO Bot+Sql. Админский режим, добавление тестов и заданий


load_dotenv()
API_TOKEN = getenv('API_TOKEN_TG')
is_logging = getenv('IS_LOGGING')

dp = Dispatcher()

db_mysql = DBMYSQL()

is_created_db = get_bool_from_str(db_mysql.DB_IS_CREATED)
is_echo_db = get_bool_from_str(db_mysql.DB_ECHO)
ic(is_created_db, is_echo_db)

async_dsn = db_mysql.get_async_dsn()
sql_async_engine = get_async_engine(async_dsn, is_echo_db)
async_session_sql_connect = async_sessionmaker(sql_async_engine)


bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
