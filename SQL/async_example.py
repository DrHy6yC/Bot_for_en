from icecream import ic
import asyncio

# from SQL.create_min_in_DB import filling_min_db
from models import UsersORM, QuizzesORM, ConstantsORM, QuizeStatusesORM
import orm


async def rewrite_DB():
    # await filling_min_db()
    pass


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
    result = await orm.async_get_user_test_by_user_tg_id_and_status(809916411, 1)
    ic(type(result.ID))
    ic(result.ID)

if __name__ == "__main__":
    # asyncio.run(rewrite_DB())
    # asyncio.run(check_db())
    asyncio.run(tasks())
