import re


def detect_en_simbol(text_check: str) -> bool:
    regex_num = re.compile('[a-zA-Z]+')
    result_func = bool(regex_num.search(text_check))
    return result_func


if __name__ == '__main__':
    text = 'лтвлтувлту'
    print(detect_en_simbol(text))
