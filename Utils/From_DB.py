from Create_bot import sql


def find_user_bd(user_tg_id: str) -> bool:
    args_proc = [user_tg_id, 0]
    USER = sql.call_procedure_from_db(args_proc)[1]
    is_user_found = bool(USER)
    return is_user_found
