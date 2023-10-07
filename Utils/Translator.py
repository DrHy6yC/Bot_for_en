import requests
import json


def detect_lang(text: str) -> str:
    import requests
    url = "https://api-b2b.backenster.com/b1/api/v3/translate"

    payload = {
        "to": "ru_RU",
        "data": text,
        "platform": "api"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "a_FpZIkZUTL1JqY3dRoy8KrBwH4pswhz53CAoOZgEXgk400VMCKqAgbhRT9li2Ho5gFp5rtPBha4m3AoCg"
    }
    response = requests.post(url, json=payload, headers=headers)
    res = json.loads(response.text)
    return res['from']


def translate_text(text: str, en_ru=False) -> str:
    """
    Default translate ru -> en
    If is_detect = False, en-ru disable
    :param text:
    :param en_ru: Switches translate en -> ru
    :return: translete in str
    """
    lang_elementary = "ru_RU"
    lang_finite = "en_GB"
    if en_ru:
        lang_elementary = "en_GB"
        lang_finite = "ru_RU"
    url = "https://api-b2b.backenster.com/b1/api/v3/translate"
    payload = {
        "from": lang_elementary,
        "to": lang_finite,
        "data": text,
        "platform": "api"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "a_FpZIkZUTL1JqY3dRoy8KrBwH4pswhz53CAoOZgEXgk400VMCKqAgbhRT9li2Ho5gFp5rtPBha4m3AoCg"
    }
    response = requests.post(url, json=payload, headers=headers)
    res = json.loads(response.text)
    return res['result']


if __name__ == '__main__':
    t = translate_text('Включить')
    print(t)
