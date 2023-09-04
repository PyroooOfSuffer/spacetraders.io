import psycopg2
from configparser import ConfigParser
from src.database import db_setup

config = ConfigParser()
config.read('config.ini')

db_name = config.get('database', 'dbname')
user = config.get('database', 'user')
password = config.get('database', 'password')
host = config.get('database', 'host')


def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )
        return conn
    except Exception as e:
        print("Error in connect_to_db():", e)
        return None


def fetch_data(table_name):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            select_from = "SELECT * FROM {}".format(table_name)

            cursor.execute(select_from)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error:", e)
        finally:
            conn.close()


def insert_sample_data_in_test(table_name, keys, values_list):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            data_strs = []
            for values in values_list:
                keys_str = ", ".join(keys)
                data_str = ", ".join(values)
                data_strs.append(f"({data_str})")

            all_data_strs = ", ".join(data_strs)
            insert_query = f"INSERT INTO {table_name} ({keys_str}) VALUES [{all_data_strs}]"
            data = [('John', 25), ('Jane', 30)]

            cursor.executemany(insert_query, data)
            conn.commit()
            print(f"Sample data inserted into {table_name} successfully")
        except Exception as e:
            print(f"Error inserting data into {table_name}:", e)
        finally:
            conn.close()


def create_table(table_name, columns_dict):
    db_setup.create_table(table_name, columns_dict)
