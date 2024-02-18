from os import getenv
import requests
from dotenv import load_dotenv


load_dotenv()


def detect_lang(text: str) -> str:
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

    payload = {"q": text}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "316f25f77emshc29da0dac219ba0p1d50b6jsn9c1c76ea8927",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response)
    result_str = response.json()['data']['detections'][0][0]['language']
    return result_str


def translate_text(text: str, en_ru=False, is_detected=False) -> str:
    """
    Default translate ru -> en
    if en_ru = True, is_detected is disabled
    :param text:
    :param en_ru: Switches translate en -> ru
    :param is_detected:
    :return: translate in str
    """
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    lang_elementary = 'ru'
    lang_finite = 'en'
    if is_detected:
        lang_elementary = detect_lang(text)
        if lang_elementary == 'en':
            lang_finite = 'ru'
    if en_ru:
        lang_elementary = 'en'
        lang_finite = 'ru'

    payload = {
        "q": text,
        "target": lang_finite,
        "source": lang_elementary
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": getenv('API_GOOGLE_TRANSLATE'),
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response)
    result_str = response.json()['data']['translations'][0]['translatedText']
    return result_str


if __name__ == '__main__':
    t = detect_lang('Переведенный текст')
    print(t)
