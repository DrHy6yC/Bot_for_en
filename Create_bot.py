from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Utils.From_DB import get_const

storage = MemoryStorage()

# TODO Bot. Реализовать запуск теста только в личку, если запускался в группе результат отправлялся еще и в группу
# TODO Bot+Sql. Разграничить пользователей по ролям
# TODO Bot+Sql. Админский режим, добавление тестов
# TODO Bot+Test+Sql. Перейти на aiogram 3.0...
API_TOKEN = get_const('API_TOKEN_TG')
MY_ID = get_const('MY_ID')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
