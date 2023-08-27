from spacetrader_api import *
from ..database import db_operations
import psycopg2


def create_token(symbol, faction, email):
    file_path = "auth_token.txt"
    response = create_new(symbol, faction, email)
    token = response["data"]["token"]

    with open(file_path, "w") as file:
        file.write(token)
    print(f"Token generated in {file_path}")


def get_ships_data():
    response = list_ships()
    if response["meta"]["total"] > response["meta"]["limit"]:
        "f"
    ship_data = response["data"]
    for ship in ship_data:
        print(ship.keys())


get_ships_data()


def infer_column_type(value):
    if isinstance(value, int):
        return "INT"
    elif isinstance(value, str):
        return "VARCHAR(255)"
    elif isinstance(value, dict):
        return "JSONB"
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")


def create_ship_table(table_name, columns):
    conn = db_operations.connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            column_definitions = ", ".join([f"{col} {infer_column_type(value)}" for col, value in columns.items()])

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
