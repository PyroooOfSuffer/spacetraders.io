import psycopg2
from configparser import ConfigParser

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
        print("Error in connect_to_db()::", e)
        return None


def drop_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host
    )
    if conn:
        try:
            conn.autocommit = True
            cursor = conn.cursor()

            drop_query = "DROP DATABASE IF EXISTS {}".format(db_name)

            cursor.execute(drop_query)
            print(f"Database {db_name} dropped successfully")
        except Exception as e:
            print(f"Error dropping database {db_name}:", e)
        finally:
            conn.close()


def create_database():
    confirmation = input(f"Are you sure you want to create the NEW database '{db_name}'? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Database creation aborted.")
        return
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host
        )
        if conn:
            try:
                drop_database()
                conn.autocommit = True
                cursor = conn.cursor()

                create_query = "CREATE DATABASE {}".format(db_name)

                cursor.execute(create_query)
                print(f"Database {db_name} created successfully")
            except Exception as e:
                print(f"Error creating database {db_name}:", e)
            finally:
                conn.close()
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)


def create_test_table():
    conn = connect_to_db()
    table_name = "test"
    if conn:
        try:
            cursor = conn.cursor()

            create_query = """
                CREATE TABLE {} (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    age INT
                );
            """.format(table_name)

            cursor.execute(create_query)
            conn.commit()
            print(f"Table {table_name} created successfully")
        except Exception as e:
            print(f"Error creating table {table_name}:", e)
        finally:
            conn.close()


def insert_sample_data_in_test():
    conn = connect_to_db()
    table_name = "test"
    if conn:
        try:
            cursor = conn.cursor()

            insert_query = "INSERT INTO {} (name, age) VALUES (%s, %s)".format(table_name)
            data = [('John', 25), ('Jane', 30)]

            cursor.executemany(insert_query, data)
            conn.commit()
            print(f"Sample data inserted into {table_name} successfully")
        except Exception as e:
            print(f"Error inserting data into {table_name}:", e)
        finally:
            conn.close()


def create_table(table_name, columns_dict):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            column_definitions = ", ".join([f"{col} {col_type}" for col, col_type in columns_dict.items()])

            create_query = f"""
                CREATE TABLE {table_name} (
                    id SERIAL PRIMARY KEY,
                    {column_definitions}
                );
            """
            cursor.execute(create_query)
            conn.commit()
            print(f"Table {table_name} created successfully")
        except Exception as e:
            print(f"Error creating table {table_name}:", e)
        finally:
            conn.close()


if __name__ == "__main__":
    create_database()
    create_test_table()
    insert_sample_data_in_test()
