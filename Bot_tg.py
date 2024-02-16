import asyncio
import logging
import sys

from Create_bot import dp, bot
from Handlers.Inline_handlers import register_inline_handler


async def main() -> None:
    register_inline_handler(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
