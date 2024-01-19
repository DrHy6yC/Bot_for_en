from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Utils.SQL_actions import SQLAction as sql

storage = MemoryStorage()

sql = sql()
API_TOKEN = sql.select_const_db('API_TOKEN_TG')
MY_ID = sql.select_const_db('MY_ID')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
