from aiogram.utils import executor
from Create_bot import dp, sql_bot
from Handlers import Callback_handlers as ch
from Handlers import Message_handler as mh
from Handlers import Inline_handlers as ih


async def on_startup(_) -> None:
    print('Run')


async def on_shutdown(_) -> None:
    print('Off')

if __name__ == '__main__':
    try:
        mh.register_handlers_user(dp)
        ch.register_call_handlers_user(dp)
        ih.register_inline_handler(dp)

        executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as error_exeption:
        print('Bot error')
        print(error_exeption)
    finally:
        sql_bot.end_con()
