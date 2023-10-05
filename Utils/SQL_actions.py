from pathlib import Path
import mysql.connector
from Utils.Read_file import import_csv
from Utils import SQL_querys as sql_q


class SQLAction:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="gfhjkzytn", database="BOT")
        self.cursor = self.conn.cursor()
        query = 'USE BOT'
        print('Start connect to BOT')
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print('Connect to BOT: done')
        except Exception as error_exept:
            print('Connect to BOT: FAILED')
            print(error_exept)

    def end_con(self) -> None:
        # print('Start end_con')
        try:
            self.cursor.close()
            self.conn.close()
            # print('Close connect: done')
            # print('End end_con')
        except Exception as error_exept:
            print('Error end_con')
            print('Close connect: FAILED')
            print(error_exept)

    def select_db(self, query: str, data: dict) -> list:
        result = list()
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        for tuple_select in tuples:
            result.append(list(tuple_select))
        return result

    def select_db_one(self, query: str, data: dict) -> str:
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        tuple_select = self.cursor.fetchone()
        result = str(tuple_select[0])
        return result

    def insert_update_db(self, query: str, data: dict) -> None:
        self.cursor.execute(query, data)
        self.conn.commit()


if __name__ == '__main__':
    sql = None
    try:
        sql = SQLAction()
        result_select = sql.select_db_one(
            sql_q.select_SURVEY_NAME_from_SURVEY)
        print(result_select)

    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
