import asyncio
import logging
import sys

from Create_bot import dp, bot
from Handlers import register_call_handlers_user
from Handlers import register_inline_handler
from Handlers import register_handlers_message


async def main() -> None:
    register_inline_handler(dp)
    register_handlers_message(dp)
    register_call_handlers_user(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
