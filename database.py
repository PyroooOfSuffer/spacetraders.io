import psycopg2

"""
create_db (db_name)

drop_db (db_name)

create_table(db_name, table_name, column_type)

drop_table(db_name, table_name)

add_data(db_name, table_name, column_value):

read_data(db_name, table_name, filter_column_value)

remove_data(db_name, table_name, filter_column_value)

search_data(db_name, table_name, filters)

update_data(db_name, table_name, update_column_value, filter_column_value)
"""


def connect_to_db(db_name):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user="postgres",
            password="X#9sP4*7qYvT",
            host="localhost"
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def create_db(db_name):
    connection = connect_to_db('postgres')
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name};")
            connection.commit()
            cursor.close()
            connection.close()
            print(f"Database '{db_name}' created successfully.")
        except psycopg2.Error as e:
            print("Error creating the database:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def drop_db(db_name):
    connection = connect_to_db('postgres')
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
            connection.commit()
            cursor.close()
            connection.close()
            print(f"Database '{db_name}' dropped successfully.")
        except psycopg2.Error as e:
            print("Error dropping the database:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def create_table(db_name, table_name, column_type):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_type});")
            connection.commit()
            cursor.close()
            print(f"Table '{table_name}' created successfully.")
        except psycopg2.Error as e:
            print("Error creating the table:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def drop_table(db_name, table_name):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            connection.commit()
            cursor.close()
            print(f"Table '{table_name}' dropped successfully.")
        except psycopg2.Error as e:
            print("Error dropping the table:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def add_data(db_name, table_name, column_value):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            columns = ', '.join(column_value.keys())
            values = ', '.join(['%s'] * len(column_value))

            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"

            cursor.execute(query, tuple(column_value.values()))
            connection.commit()
            cursor.close()
            print("Data added successfully.")
        except psycopg2.Error as e:
            print("Error adding data:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def read_data(db_name, table_name, filter_column_value=None):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            if filter_column_value is not None:
                query = f"SELECT * FROM {table_name} WHERE id = %s;"
                cursor.execute(query, (filter_column_value,))
            else:
                query = f"SELECT * FROM {table_name};"
                cursor.execute(query)

            result = cursor.fetchall()

            cursor.close()
            return result
        except psycopg2.Error as e:
            print("Error reading data:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def remove_data(db_name, table_name, filter_column_value):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            where_clause = " AND ".join([f"{key} = %s" for key in filter_column_value.keys()])
            query = f"DELETE FROM {table_name} WHERE {where_clause};"

            cursor.execute(query, tuple(filter_column_value.values()))
            connection.commit()
            cursor.close()
            print("Data removed successfully.")
        except psycopg2.Error as e:
            print("Error removing data:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def search_data(db_name, table_name, filters):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            where_clause = " AND ".join([f"{key} = %s" for key in filters.keys()])
            query = f"SELECT * FROM {table_name} WHERE {where_clause};"

            cursor.execute(query, tuple(filters.values()))
            result = cursor.fetchall()

            cursor.close()
            return result
        except psycopg2.Error as e:
            print("Error searching data:", e)
    else:
        print("Could not connect to the PostgreSQL server.")


def update_data(db_name, table_name, update_column_value, filter_column_value):
    connection = connect_to_db(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            set_clause = ", ".join([f"{key} = %s" for key in update_column_value.keys()])

            where_clause = " AND ".join([f"{key} = %s" for key in filter_column_value.keys()])

            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause};"

            cursor.execute(query, tuple(update_column_value.values()) + tuple(filter_column_value.values()))
            connection.commit()
            cursor.close()
            print("Data updated successfully.")
        except psycopg2.Error as e:
            print("Error updating data:", e)
    else:
        print("Could not connect to the PostgreSQL server.")
