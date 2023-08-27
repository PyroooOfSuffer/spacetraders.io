from spacetrader_api import *
#  from ..database import db_operations
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
    for (key, value) in ship_data[0].items():

        print(f"key: {key}, value type: {infer_column_type(value)}")


def infer_column_type(value):
    if isinstance(value, int):
        return "INT"
    elif isinstance(value, str):
        return "VARCHAR(255)"
    elif isinstance(value, dict):
        return "JSONB"
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")


#  should look like this I think:
#  db_operations.create_table(a, a, infer_column_type())

get_ships_data()