from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode

# TODO Bot. Проработать обычные кнопки для лички и для группы
# TODO Bot. Реализовать запуск теста только в личку, если запускался в группе результат отправлялся еще и в группу
# TODO Bot+Sql. Разграничить пользователей по ролям
# TODO Bot+Sql. Админский режим, добавление тестов и заданий
# TODO Bot+Test+Sql. Перейти на aiogram 3.0...


load_dotenv()
API_TOKEN = getenv('API_TOKEN_TG')

dp = Dispatcher()
inline_router = Router()
bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
