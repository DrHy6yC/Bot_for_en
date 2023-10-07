from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Utils.SQL_actions import SQLAction as sql
from Utils import SQL_querys as query

storage = MemoryStorage()

sql = sql()
API_TOKEN = sql.select_db_one(query.select_all_from_CONSTANTS_by_CONSTANT_NAMES, {'CONSTANT_NAMES': 'API_TOKEN_TG'})
MY_ID = sql.select_db_one(query.select_all_from_CONSTANTS_by_CONSTANT_NAMES, {'CONSTANT_NAMES': 'MY_ID'})

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
