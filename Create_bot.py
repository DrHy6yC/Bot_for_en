from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Utils.From_DB import get_const

storage = MemoryStorage()

API_TOKEN = get_const('API_TOKEN_TG')
MY_ID = get_const('MY_ID')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
