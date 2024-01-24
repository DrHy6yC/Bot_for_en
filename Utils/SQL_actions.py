import mysql.connector
from Utils import SQL_querys as query


# TODO  обработка исключения если запрос выдает пустоту, избавиться от класса(переработать)
# TODO Переделать класс и перекинуть лишнее в FROM_DB


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
            print('Connect to Bot: close')
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

    def call_procedure_return_one_from_db(self, name_proc: str, args_procedure: list) -> str:
        """
           Запускает процедуру SQL, результатом которой, является вывод одной ячейки в строку.
           Так как self.cursor.callproc выдает tuple из всех аргументов процедуры,
           выходной, нужный нам - последний, поэтому [-1]
           :param name_proc: Имя процедуры
           :param args_procedure: Входные и выходные параметры процедуры
           :return: Одна ячейка таблицы конвертированая в str
           """
        result_args = str(self.cursor.callproc(name_proc, args_procedure)[-1])
        return result_args

    def call_procedure_changed_db(self, name_proc: str, args_procedure: list) -> None:
        self.cursor.callproc(name_proc, args_procedure)
        self.conn.commit()

    def call_procedure_return_table(self, name_proc: str, args_procedure: list) -> list:
        result = list()
        self.cursor.callproc(name_proc, args_procedure)
        for tables in self.cursor.stored_results():
            tuples = tables.fetchall()
            for tuple_select in tuples:
                result.append(list(tuple_select))
        return result


sql = SQLAction()

if __name__ == '__main__':
    from Utils import SQL_querys as querys
    try:
        sql = SQLAction()
        args_proc = [1, 2, 0]
        r = sql.call_procedure_return_one_from_db('get_question', args_proc)
        print(r)

    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
