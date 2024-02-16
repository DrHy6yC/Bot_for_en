import csv


def import_csv(file_name_csv: str) -> list:
    with open(file_name_csv, "r", newline="") as file:
        dict_reader_ext = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_NONE)
        export_list = list()
        for row_dict_ext in dict_reader_ext:
            export_list.append(row_dict_ext)
    return export_list


if __name__ == "__main__":
    from pathlib import Path

    name = 'miniTest.csv'
    path = Path(__file__).parent.parent/f"Tests/{name}"
    print(str(path))
    c = import_csv(str(path))
