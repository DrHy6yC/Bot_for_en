import csv


def import_csv(path_csv: str) -> list:
    if type(path_csv) != str:
        raise TypeError("path_csv должна быть строка!")
    with open(path_csv, "r", newline="") as file:
        dict_reader_ext = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_NONE)
        export_list = list()
        for row_dict_ext in dict_reader_ext:
            export_list.append(row_dict_ext)
    return export_list
