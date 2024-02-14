import sys

from aiogram.dispatcher.filters import IDFilter
from icecream import ic

from Create_bot import dp
from aiogram import executor, types
from Handlers import Callback_handlers as ch
from Handlers import Message_handler as mh
from Handlers import Inline_handlers as ih


async def on_startup(_) -> None:
    print('Run')


async def on_shutdown(_) -> None:
    print('Off')

if __name__ == '__main__':
    mh.register_handlers_user(dp)
    ch.register_call_handlers_user(dp)
    ih.register_inline_handler(dp)


    @dp.message_handler()
    async def echo(message: types.Message):
        ic(message.from_user.id)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
