import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import sessionmaker

from SQL.Create_SQL import get_engine, get_async_engine, filling_min_db
from SQL.Database import DBMYSQL

# TODO Bot. Проработать обычные кнопки для лички и для группы
# TODO Bot. Реализовать запуск теста только в личку, если запускался в группе результат отправлялся еще и в группу
# TODO Bot+Sql. Разграничить пользователей по ролям
# TODO Bot+Sql. Админский режим, добавление тестов и заданий
# TODO Bot+Test+Sql. Перейти на aiogram 3.0...


load_dotenv()
API_TOKEN = getenv('API_TOKEN_TG')

dp = Dispatcher()
# inline_router = Router()

db_mysql = DBMYSQL()
is_created_db = db_mysql.get_db_is_created()
is_echo_db = db_mysql.get_db_is_echo()
# sync
dsn = db_mysql.get_dsn()
sql_engine = get_engine(dsn, is_echo_db)
session_sql_connect = sessionmaker(sql_engine)

# async
async_dsn = db_mysql.get_async_dsn()
sql_async_engine = get_async_engine(async_dsn, is_echo_db)
async_session_sql_connect = async_sessionmaker(sql_async_engine)

if is_created_db:
    asyncio.run(filling_min_db(sql_async_engine))
bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
