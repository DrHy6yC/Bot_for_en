from icecream import ic
import asyncio

from SQL.Create_min_in_DB import filling_min_db
# from SQL.create_min_in_DB import filling_min_db
from Models import UsersORM, QuizzesORM, ConstantsORM, QuizeStatusesORM
import ORM


async def rewrite_DB():
    await filling_min_db()


async def check_db():
    users = await orm.async_select_from_db(UsersORM)
    quizzes = await orm.async_select_from_db(QuizzesORM)
    consts = await orm.async_select_from_db(ConstantsORM)
    for user in users:
        ic(user.USER_LOGIN)
    for quize in quizzes:
        ic(quize.QUIZE_NAME)
    for const in consts:
        ic(const.CONSTANT_NAME)


async def tasks():
    result = await orm.async_get_text_level(45)
    ic(type(result))
    ic(result)

if __name__ == "__main__":
    asyncio.run(rewrite_DB())
    # asyncio.run(check_db())
    # asyncio.run(tasks())