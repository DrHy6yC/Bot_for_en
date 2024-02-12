from SQL.config import sql_async_engine
from SQL.models import QuizzesORM, ConstantsORM, QuizeStatusesORM
from SQL.orm import async_create_all_table, async_insert_data_list_to_bd


async def filling_min_db() -> None:
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

    grammar_level_test = QuizzesORM(
        QUIZE_NAME='English Level test. Grammar',
        QUIZE_DESCRIPTION='Тест для проверки уровня грамматики по английскому'
    )

    TEXT_HI = ConstantsORM(
        CONSTANT_NAME='TEXT_HI',
        CONSTANT_VALUE=hi_txt
    )

    TEXT_HELP = ConstantsORM(
        CONSTANT_NAME='TEXT_HELP',
        CONSTANT_VALUE=help_txt
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

    await async_create_all_table(sql_async_engine)
    await async_insert_data_list_to_bd([
        grammar_level_test,
        TEXT_HI, TEXT_HELP,
        status_quize_Selected, status_quize_Launched, status_quize_Stopped,
        status_quize_Revoked, status_quize_Completed, status_quize_Deleted])
