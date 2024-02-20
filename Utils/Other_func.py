def get_bool_from_str(param: str) -> bool:
    """
    Переводит строку из .env в python bool
    :return: Возвращает True когда param=True, в остальных случаях -> False
    """
    if param == 'True':
        return True
    else:
        return False
