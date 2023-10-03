from pathlib import Path
import mysql.connector
from Utils.Read_file import import_csv


class SQL_COM:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="gfhjkzytn", database="BOT")
        self.cursor = self.conn.cursor()
        query = 'USE BOT'
        print('Start connect to BOT')
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print('Connect to BOT: done')
        except Exception as error_exeption:
            print('Connect to BOT: FAILED')
            print(error_exeption)

    def end_con(self) -> None:
        # print('Start end_con')
        try:
            self.cursor.close()
            self.conn.close()
            # print('Close connect: done')
            # print('End end_con')
        except Exception as error_exeption:
            print('Error end_con')
            print('Close connect: FAILED')
            print(error_exeption)

    def select_cell_from_table(self, table: str, column_condition: str, column_result: str, value: str) -> list:
        # print('Start select_cell_from_table')
        try:
            query = f"""
            SELECT {column_result} FROM {table}
            WHERE {column_condition} = '{value}';
            """
            result_list = list()
            print(f'Выполнено выражение:\n{query}')
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for i in result:
                result_list.append(i[0])
            # print('Send result list')
            # print('End select_cell_from_table')
            return result_list
        except Exception as error_exeption:
            print('Error select_cell_from_table')
            print(error_exeption)

    def select_column_table(self, table: str, column_result: str) -> list:
        # print('Start select_column_table')
        try:
            query = f"""
            SELECT {column_result} FROM {table};
            """
            result_list = list()
            self.cursor.execute(query)
            # print(f'Выполнено выражение:\n{query}')
            result = self.cursor.fetchall()
            for i in result:
                result_list.append(i[0])
            # print('Send result list')
            # print('End select_column_table')
            return result_list
        except Exception as error_exeption:
            print('Error select column table')
            print(error_exeption)

    def select_table_with_condition(self, table: str, condition: dict) -> list:
        # print('Start select_table_with_condition')
        condition_txt = ''
        for i in condition:
            condition_txt += f" and {i} = {condition[i]}"

        try:
            result_list = list()
            query = f"""
                    SELECT * FROM {table}
                    WHERE 1=1 {condition_txt};
                    """
            # print(f'Выполнено выражение:\n{query}')
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for i in result:
                result_list.append(list(i))
            # print('Send result list')
            # print('End select_table_with_condition')
            return list(result_list)
        except Exception as error_exeption:
            print('Error select_table_with_condition')
            print(error_exeption)

    def select_table_with_condition_first_row(self, table: str, condition: dict):
        result_list = self.select_table_with_condition(table, condition)[0]
        return result_list

    def insert_row_in_table(self, table: str, columns: tuple, values: tuple) -> None:
        # print('Start insert_row_in_table')
        try:
            # columns tuple -> str
            query = f"""
                        INSERT INTO {table} ({', '.join(columns)})
                        VALUES {values};
                    """
            print(f'Выполнено выражение:\n{query}')
            self.cursor.execute(query)
            self.conn.commit()
            # print('Finish insert')
            # print('End insert_row_in_table')
        except Exception as error_exeption:
            print('Error insert_row_in_table')
            print('Error insert')
            print(error_exeption)

    def update_table(self, table: str, change_values: dict, conditions: dict) -> None:
        try:
            change_values_txt = ''
            condition_txt = ''
            for condition in conditions:
                print(condition, conditions[condition], conditions)
                condition_txt += f" and {condition} = {conditions[condition]}"
            print(condition_txt)
            j = 1
            for value in change_values:
                print(j, value, change_values[value], change_values)
                change_values_txt += f" {value} = {change_values[value]}"
                print(len(change_values))
                if j != len(change_values):
                    change_values_txt += ','
                j += 1
            print(change_values_txt)
            query = f"""UPDATE {table}  SET {change_values_txt} WHERE 1=1 {condition_txt};"""
            print(f'Выражение:\n{query}')
            self.cursor.execute(query)
            self.conn.commit()
            # print('Finish insert')
            # print('End insert_row_in_table')
        except Exception as error_exeption:
            print('Error insert_row_in_table')
            print('Error insert')
            print(error_exeption)

    def get_constant(self, constant: str) -> str:
        # print('Start get_constant')
        result = ''
        try:
            # Выводим первое значение в строку (list->tuple->str)
            result = str(self.select_cell_from_table('CONSTANTS', 'CONSTANT_NAMES', 'CONSTANT_VALUES', constant)[0])
            # print('End get_constant')
            # print('Send result str')
            return result
        except Exception as error_exeption:
            print('Error get_constant')
            print(error_exeption)
            print('Send result str')
            return result

    def import_survey_bd(self, file_name: str) -> None:
        # print('Start import_survey_bd')
        try:
            path = Path(__file__).parent / f"../{file_name}"
            csv = import_csv(path)
            # print('Start insert survey in bd')
            name = file_name.replace('.csv', '')
            name_tb_surveys = 'SURVEYS'
            name_tb_surveys_answers = 'SURVEYS_ANSWERS'
            col = ('SURVEY_NAME', 'SURVEY_DESCRIPTION')
            val = (name, 'Test for level English')
            sql.insert_row_in_table(name_tb_surveys, col, val)
            id_survey = int(sql.select_cell_from_table(name_tb_surveys, 'SURVEY_NAME', 'SURVEY_ID', name)[0])

            for i in csv:
                num_question = i['NumberQuestion']
                question = i['Question']
                answer_1 = i['Answer1']
                answer_2 = i['Answer2']
                answer_3 = i['Answer3']
                answer_4 = i['Answer4']
                true_answer = i['TrueAnswer']
                col_sa = ('SURVEY_ID', 'NUMBER_QUESTION', 'SURVEY_QUESTION', 'SURVEY_ANSWER_1',
                          'SURVEY_ANSWER_2', 'SURVEY_ANSWER_3', 'SURVEY_ANSWER_4', 'SURVEY_ANSWER_TRUE')
                val_sa = (id_survey, num_question, question, answer_1, answer_2, answer_3, answer_4, true_answer)
                sql.insert_row_in_table(name_tb_surveys_answers, col_sa, val_sa)
            # print('Finish insert survey to bd')
            # print('End import_survey_bd')
        except Exception as error_exeption:
            print('Error import_survey_bd')
            print('Error insert survey to bd')
            print(error_exeption)


if __name__ == '__main__':
    try:
        sql = SQL_COM()
        print(sql.select_cell_from_table('USER_SURVEYS', 'ID_USER', 'ID_SURVEY', '809916411'))
    except Exception as error_exeption:
        print('Error main file')
        print(error_exeption)
    finally:
        sql.end_con()
