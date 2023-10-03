from aiogram import Bot, Dispatcher
from Utils.SQL_commands import SQL_COM
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

sql_bot = SQL_COM()

API_TOKEN = sql_bot.get_constant('API_TOKEN')
MY_ID = sql_bot.get_constant('MY_ID')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


