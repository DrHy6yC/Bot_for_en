import logging
import sys

from asyncio import run
from icecream import ic

from Create_bot import dp, bot, is_created_db, sql_async_engine, is_logging
from Utils import get_bool_from_str
from Handlers import register_call_handlers_user
from Handlers import register_inline_handler
from Handlers import register_handlers_message
from SQL.ORM import filling_min_db


async def main() -> None:
    register_inline_handler(dp)
    register_handlers_message(dp)
    register_call_handlers_user(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


async def on_startup():
    ic(is_created_db)
    if is_created_db:
        await filling_min_db(sql_async_engine)
        ic('База пересоздана')
    ic('Бот Запущен')


async def on_shutdown():
    ic('Бот остановлен')


if __name__ == "__main__":
    if get_bool_from_str(is_logging):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(main())
