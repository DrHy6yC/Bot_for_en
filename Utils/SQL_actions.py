import mysql.connector
from Utils import SQL_querys as query


# TODO  обработка исключения если запрос выдает пустоту, избавиться от класса(переработать)
class SQLAction:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="gfhjkzytn", database="BOT")
        self.cursor = self.conn.cursor()
        query_text = 'USE BOT'
        print('Start connect to BOT')
        try:
            self.cursor.execute(query_text)
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

    def select_db_one(self, query: str, data: dict) -> str:
        try:
            self.select_db(query, data)
            result = self.select_db(query, data)[0][0]
            return result
        except Exception as error_exception_sql:
            print(error_exception_sql)
            return ''

    def insert_update_delete_db(self, query: str, data: dict) -> None:
        self.cursor.execute(query, data)
        self.conn.commit()

    def select_const_db(self, name_const: str) -> str:
        try:
            name = self.select_db_one(
                                   query=query.select_all_from_CONSTANTS_by_CONSTANT_NAMES,
                                   data={'CONSTANT_NAMES': name_const})
            return name
        except Exception as error_exception_sql:
            print(error_exception_sql)
            return ''
    def find_user_bd(self, user_tg_id: str) -> bool:
        USER = self.select_db_one(
            query=query.select_USER_TG_ID_from_USERS_by_USER_TG_ID,
            data={'USER_TG_ID': user_tg_id})
        is_user_found = bool(USER)
        return is_user_found

    def insert_user_bd(self, user_tg_id: str, user_full_name: str, username: str) -> None:
        data = {'USER_TG_ID': user_tg_id, 'USER_FULL_NAME': user_full_name, 'USER_LOGIN': username}
        self.insert_update_delete_db(
            query=query.insert_USERS_by_USER_TG_ID_and_USER_FULL_NAME_and_USER_LOGIN,
            data=data)

    def delete_user_bd(self, user_tg_id: str) -> None:
        data = {'USER_TG_ID': user_tg_id}
        self.insert_update_delete_db(
            query=query.delete_USER_from_USERS_by_USER_TG_ID,
            data=data)


if __name__ == '__main__':
    sql = None
    try:
        sql = SQLAction()
        sql.insert_user_bd('809916411', 'efnef fef', 'Dr_Hy6yC')
        # result_select = sql.find_user_bd('809916411')
        # print(result_select)

    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
