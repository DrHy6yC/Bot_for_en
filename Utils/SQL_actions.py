import mysql.connector


# TODO Sql. Обработка исключения если запрос выдает пустоту
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

    def call_procedure_return_changed_one(self, name_proc: str, args_procedure: list) -> str:
        result_args = str(self.cursor.callproc(name_proc, args_procedure)[-1])
        self.conn.commit()
        return str(result_args)


# TODO Sql. Реализовать подключение и отключение коннекта в вызовах процедуры
sql = SQLAction()

if __name__ == '__main__':
    try:
        sql = SQLAction()
        args_proc = [5436880841, 0]
        r = sql.call_procedure_return_one_from_db('get_is_user_in_bd', args_proc)
        print(r)

    except Exception as error_exception:
        print('Error main file')
        print(error_exception)
    finally:
        sql.end_con()
