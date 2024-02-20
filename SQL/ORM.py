import datetime
from typing import Union

from icecream import ic

from sqlalchemy import select, func, and_, desc
from sqlalchemy.orm import join
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.sql.functions import count

from Create_bot import async_session_sql_connect
from SQL.Models import Base, UsersORM, QuizzesORM,  UserQuizzesORM, \
    QuizeAnswersORM, QuizeQuestionsORM, UserAnswersORM, QuizeTrueAnswersORM

from SQL.Models import ConstantsORM, QuizeStatusesORM, UserLevelsORM
from Utils.Import_csv_to_bd import async_import_survey_csv

ModelsORM = UsersORM, QuizzesORM, ConstantsORM, UserQuizzesORM, UserLevelsORM, QuizeAnswersORM, \
    QuizeQuestionsORM, UserAnswersORM


# Example:
# ================================async===================================
async def async_create_all_table(async_engine: AsyncEngine) -> None:
    """
    Пересоздает(Если есть) все таблицы наследуемые от Base
    :param async_engine: Принимает sql_async_engine/подключение
    :return: Ничего не возвращает
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_insert_data_list_to_bd(list_data: list[Union[ModelsORM]]) -> None:
    async with async_session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        await session_sql.commit()


async def async_insert_and_get_modelORM(model_orm: Union[ModelsORM]) -> Union[ModelsORM]:
    async with async_session_sql_connect() as session_sql:
        session_sql.add_all([model_orm])
        await session_sql.get(model_orm.__class__, model_orm.ID)
        await session_sql.commit()
        return model_orm


async def async_select_from_db(class_orm: Union[ModelsORM]) -> list[Union[ModelsORM]]:
    async with async_session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().all()
        return result


async def async_get_orm_by_pk(class_orm: Union[ModelsORM], id_orm: int) -> Union[ModelsORM]:
    async with async_session_sql_connect() as session_sql:
        result = await session_sql.get(class_orm.__class__, id_orm)
        return result


async def async_update_object(model_orm, new_user_param: str) -> None:
    async with async_session_sql_connect() as session_sql:
        model_orm = await session_sql.get(model_orm.__class__, model_orm.ID)
        model_orm.USER_LOGIN = new_user_param
        await session_sql.commit()


async def async_update_running_test_num_question(id_running_test: int, num_question: int) -> None:
    async with async_session_sql_connect() as session_sql:
        user_test = await session_sql.get(UserQuizzesORM, id_running_test)
        user_test.QUESTION_NUMBER = num_question
        await session_sql.commit()


async def async_update_running_test_score(id_running_test: int, score: int) -> None:
    async with async_session_sql_connect() as session_sql:
        user_test = await session_sql.get(UserQuizzesORM, id_running_test)
        user_test.QUIZE_SCORE = score
        await session_sql.commit()


async def async_get_const(name_const: str) -> ConstantsORM:
    async with async_session_sql_connect() as session_sql:
        query = select(ConstantsORM).where(ConstantsORM.CONSTANT_NAME == name_const)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one()
        return result


async def async_select_user_by_id(user_tg_id: int) -> UsersORM:
    async with async_session_sql_connect() as session_sql:
        query = select(UsersORM).where(UsersORM.USER_TG_ID == user_tg_id)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one()
        return result


async def async_is_user_in_bd(user_tg_id: int) -> bool:
    async with async_session_sql_connect() as session_sql:
        query = select(UsersORM).where(UsersORM.USER_TG_ID == user_tg_id)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one_or_none()
        if result:
            return True
        else:
            return False


async def async_get_name_test() -> list[str]:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM.QUIZE_NAME).select_from(QuizzesORM)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().all()
    return result


async def async_get_name_test_by_id(id_test) -> list[str]:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM.QUIZE_NAME).select_from(QuizzesORM).where(QuizzesORM.ID == id_test)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one_or_none()
    return result


async def async_get_is_user_status_test(user_tg_id: int, status: int) -> bool:
    async with async_session_sql_connect() as session_sql:
        query = select(func.count(UserQuizzesORM.ID)).\
            select_from(UserQuizzesORM).\
            where(and_(UserQuizzesORM.ID_USER_TG == user_tg_id, UserQuizzesORM.QUIZE_STATUS == status))
        user_exec = await session_sql.execute(query)
        user = user_exec.scalars().one_or_none()
    is_user_status_test: bool = user != 0
    return is_user_status_test


async def async_get_user_test_by_user_tg_id_and_status(user_tg_id: int, status: int) -> UserQuizzesORM:
    async with async_session_sql_connect() as session_sql:
        query = select(UserQuizzesORM).\
            select_from(UserQuizzesORM).\
            where(and_(UserQuizzesORM.ID_USER_TG == user_tg_id, UserQuizzesORM.QUIZE_STATUS == status)).\
            order_by(desc(UserQuizzesORM.CREATE_TIME))
        users_exec = await session_sql.execute(query)
        user = users_exec.scalars().first()
        return user


async def async_get_id_test(name_test: str) -> int:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM.ID).\
            select_from(QuizzesORM).\
            where(QuizzesORM.QUIZE_NAME == name_test)
        tests_exec = await session_sql.execute(query)
        test = tests_exec.scalars().first()
        return test


async def async_set_user_test_status(user_test_id: int, status: int) -> None:
    async with async_session_sql_connect() as session_sql:
        test = await session_sql.get(UserQuizzesORM, user_test_id)
        if test:
            test.QUIZE_STATUS = status
        else:
            ic(f"Теста id = {user_test_id} со статусом = {status} нет.")
        ic(user_test_id, status)
        await session_sql.commit()


async def async_set_user_level(user_tg_id: int, level: int) -> None:
    async with async_session_sql_connect() as session_sql:
        query = select(UsersORM).where(UsersORM.USER_TG_ID == user_tg_id)
        user_exec = await session_sql.execute(query)
        user = user_exec.scalars().first()
        user.USER_LEVEL = level
        await session_sql.commit()


async def async_get_level_user_text(user_tg_id: int) -> str:
    async with async_session_sql_connect() as session_sql:
        query = select(UserLevelsORM.LEVEL_TEXT). \
            select_from(join(UserLevelsORM, UsersORM)). \
            where(UsersORM.USER_TG_ID == user_tg_id)
        text_exec = await session_sql.execute(query)
        text = text_exec.scalars().first()
        return text


async def async_is_test_in_bd(name_test: int) -> bool:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM).where(QuizzesORM.QUIZE_NAME == name_test)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().one_or_none()
        if result:
            return True
        else:
            return False


async def async_get_test_by_name(name_test: str) -> QuizzesORM:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizzesORM).where(QuizzesORM.QUIZE_NAME == name_test)
        test_execute = await session_sql.execute(query)
        test = test_execute.scalars().first()
        return test


async def async_get_answers_by_id_test_and_num_question(id_test: int, num_question: int) -> list[QuizeAnswersORM]:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizeAnswersORM).where(
            and_(QuizeAnswersORM.ID_QUIZE == id_test, QuizeAnswersORM.QUESTION_NUMBER == num_question)
        )
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().all()
        return result


async def async_get_count_question_test(id_test: int) -> int:
    async with async_session_sql_connect() as session_sql:
        query = select(count(QuizeQuestionsORM.ID)).where(QuizeQuestionsORM.ID_QUIZE == id_test)
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().first()
        return result


async def async_get_question_by_id_test_num_question(id_test: int, num_question: int) -> str:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizeQuestionsORM.QUESTION_TEXT).where(
            and_(QuizeQuestionsORM.ID_QUIZE == id_test, QuizeQuestionsORM.QUESTION_NUMBER == num_question))
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().first()
        return result


async def async_get_text_level(points: float) -> list[int, str]:
    async with async_session_sql_connect() as session_sql:
        query = select(UserLevelsORM).where(
            and_(UserLevelsORM.MIN_LEVEL_SCORE <= points, UserLevelsORM.MAX_LEVEL_SCORE >= points))
        result_execute = await session_sql.execute(query)
        user_level = result_execute.scalars().first()
        result = [user_level.ID, user_level.LEVEL_TEXT]
        return result


async def async_get_answer_text_by_id(id_answer: int) -> str:
    async with async_session_sql_connect() as session_sql:
        answer = await session_sql.get(QuizeAnswersORM, id_answer)
        result = answer.ANSWER_TEXT
        return result


async def get_true_answer_id_by_id_test_and_num_question(id_test: int, num_question: str) -> int:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizeTrueAnswersORM.ID_ANSWER).where(
            and_(QuizeTrueAnswersORM.ID_QUIZE == id_test, QuizeTrueAnswersORM.QUESTION_NUMBER == num_question))
        result_execute = await session_sql.execute(query)
        result = result_execute.scalars().first()
        return result


async def async_get_user_answer(user_test_id: int, num_question: int) -> UserAnswersORM:
    async with async_session_sql_connect() as session_sql:
        query = select(UserAnswersORM).\
            where(
            and_(UserAnswersORM.ID_USER_QUIZE == user_test_id, UserAnswersORM.QUESTION_NUMBER == num_question)
        )
        user_answer_execute = await session_sql.execute(query)
        user_answer = user_answer_execute.scalars().first()
        return user_answer


async def async_get_true_answer(test_id: int, num_question: int) -> QuizeTrueAnswersORM:
    async with async_session_sql_connect() as session_sql:
        query = select(QuizeTrueAnswersORM).\
            where(
            and_(QuizeTrueAnswersORM.ID_QUIZE == test_id, QuizeTrueAnswersORM.QUESTION_NUMBER == num_question)
        )
        user_answer_execute = await session_sql.execute(query)
        user_answer = user_answer_execute.scalars().first()
        return user_answer


async def async_get_user_test_by_id(user_test_id: int) -> UserQuizzesORM:
    async with async_session_sql_connect() as session_sql:
        user_test = await session_sql.get(UserQuizzesORM, user_test_id)
        return user_test


async def filling_min_db(sql_async_engine) -> None:
    """
        Функция для перезаписи БД и заполнение необходимых параметров для начала работы бота:

        * Константы
        * Тесты
        * Уровни

    """
    help_txt = """  
    Этот бот умеет:

    * Переводить словосочетания в инлайн режиме если упомянуть @English_bot_help_HW_bot в сообщениях;

    * Ещё запускать тесты, которые подскажут твой уровень знания английского (Грамматика). 

    В скором времени будет напоминать о тех словах что нужно выучить.
    """

    hi_txt = """   
    Привет, @FIO! Это бот который проверит твои знания по английскому языку.

    Используй кнопку помощи, если хочешь узнать что может бот сейчас.

    Или переходи сразу к тесту и удивись своему уровню!
    """

    TEXT_HI = ConstantsORM(
        CONSTANT_NAME='TEXT_HI',
        CONSTANT_VALUE=hi_txt
    )

    TEXT_HELP = ConstantsORM(
        CONSTANT_NAME='TEXT_HELP',
        CONSTANT_VALUE=help_txt
    )

    CREATE_TIME_BD = ConstantsORM(
        CONSTANT_NAME='CREATE_TIME_BD',
        CONSTANT_VALUE=str(datetime.datetime.now())
    )

    status_quize_Selected = QuizeStatusesORM(
        ID=1,
        STATUS_TEXT='Selected'
    )

    status_quize_Launched = QuizeStatusesORM(
        ID=2,
        STATUS_TEXT='Launched'
    )
    status_quize_Stopped = QuizeStatusesORM(
        ID=3,
        STATUS_TEXT='Stopped'
    )
    status_quize_Revoked = QuizeStatusesORM(
        ID=4,
        STATUS_TEXT='Revoked'
    )
    status_quize_Completed = QuizeStatusesORM(
        ID=5,
        STATUS_TEXT='Completed'
    )

    status_quize_Deleted = QuizeStatusesORM(
        ID=6,
        STATUS_TEXT='Deleted'
    )

    level_A0 = UserLevelsORM(
        LEVEL_TEXT='No level',
        MIN_LEVEL_SCORE=0,
        MAX_LEVEL_SCORE=5
    )

    level_A1 = UserLevelsORM(
        LEVEL_TEXT='Beginner (A1)',
        MIN_LEVEL_SCORE=6,
        MAX_LEVEL_SCORE=30
    )

    level_A2 = UserLevelsORM(
        LEVEL_TEXT='Elementary (A2)',
        MIN_LEVEL_SCORE=31,
        MAX_LEVEL_SCORE=60
    )

    level_B1 = UserLevelsORM(
        LEVEL_TEXT='Pre-Intermediate (B1)',
        MIN_LEVEL_SCORE=61,
        MAX_LEVEL_SCORE=90
    )

    level_B2 = UserLevelsORM(
        LEVEL_TEXT='Intermediate (B2)',
        MIN_LEVEL_SCORE=91,
        MAX_LEVEL_SCORE=100
    )

    await async_create_all_table(sql_async_engine)
    await async_insert_data_list_to_bd([
        TEXT_HI, TEXT_HELP, CREATE_TIME_BD,
        status_quize_Selected, status_quize_Launched, status_quize_Stopped,
        status_quize_Revoked, status_quize_Completed, status_quize_Deleted,
        level_A0, level_A1, level_A2, level_B1, level_B2,
    ])

    await async_import_survey_csv("English Level test. Grammar.csv",
                                  "Основной тест для проверки уровня английского (грамматика)")

    await async_import_survey_csv("Who test.csv",
                                  "Микро тест для проверки работоспособности теста")