def get_bool_from_str(text: str) -> bool:
    """
    Переводит строку из .env в python bool
    :return: Возвращает True когда param=True, в остальных случаях -> False
    """
    result: bool = False
    if text.lower() == "true":
        result = True
    return result
