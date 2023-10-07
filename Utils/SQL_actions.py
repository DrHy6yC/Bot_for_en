import mysql.connector
from Utils import SQL_querys as querys


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
        except Exception as error_except:
            print('Connect to BOT: FAILED')
            print(error_except)

    def end_con(self) -> None:
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as error_except:
            print('Error end_con')
            print('Close connect: FAILED')
            print(error_except)

    def select_db(self, query: str, data: dict) -> list:
        result = list()
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        for tuple_select in tuples:
            # result.append(tuple_select)
            result.append(list(tuple_select))
        return result

    def select_db_one(self, query: str, data: dict) -> list:
        self.select_db(query, data)
        result = self.select_db(query, data)[0][0]
        return result

    def insert_update_db(self, query: str, data: dict) -> None:
        self.cursor.execute(query, data)
        self.conn.commit()


if __name__ == '__main__':
    sql = None
    try:
        sql = SQLAction()
        result_select =sql.select_db_one(querys.select_all_from_CONSTANTS_by_CONSTANT_NAMES,
                                         {'CONSTANT_NAMES': 'API_TOKEN_TG'})

        print(result_select)

    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
