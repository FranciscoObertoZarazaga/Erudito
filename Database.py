import mysql.connector as db


class DataBase:
    def __init__(self):
        self.conection = db.connect(
            host='rm-2ev2pd8w385r421784o.mysql.rds.aliyuncs.com',
            user='trader23_usr',
            password='excitingTimes23!',
            database='trader23_db',
            port=3306
        )
        self.cursor = self.conection.cursor()

    def insert(self, table_name, columns, values):
        try:
            self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
            self.conection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, table_name):
        try:
            self.cursor.execute('SELECT * FROM ' + table_name + ' LIMIT 10')
            return list(self.cursor.fetchall())
        except Exception as e:
            print(e)

    def select_with(self, table_name, param, value):
        if not isinstance(param, list):
            param = [param]
        if not isinstance(value, list):
            value = [value]
        assert len(param) == len(value)
        try:
            command = f'SELECT * FROM {table_name} WHERE 1=1'
            for p, v in zip(param, value):
                command += f" and {p}='{v}'"
            self.cursor.execute(command)
            return list(self.cursor.fetchall())
        except Exception as e:
            print(e)

    def update(self, name_table, name, value, id_value, id_name='id'):
        try:
            self.cursor.execute(f"UPDATE {name_table} SET {name} = '{value}' where {id_name} = '{id_value}'")
            self.conection.commit()
        except Exception as e:
            print(e)

    def delete_all(self, table_name):
        try:
            self.cursor.execute('DELETE FROM ' + table_name)
        except Exception as e:
            print(e)

    def close(self):
        self.conection.close()

    def get_connection(self):
        return self.conection

    def count(self, table, user_id):
        try:
            self.cursor.execute(f'SELECT count(*) FROM {table} WHERE user_id={user_id}')
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)


DATABASE = DataBase()
