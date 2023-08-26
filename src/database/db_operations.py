import psycopg2
from configparser import ConfigParser

config = ConfigParser()
config.read('../../config.ini')

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


def fetch_data():
    conn = connect_to_db()
    table_name = "test"
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
