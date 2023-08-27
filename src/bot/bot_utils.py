from spacetrader_api import *
import sys
sys.path.append("../database")
import db_operations


def create_token(symbol, faction, email):
    file_path = "auth_token.txt"
    response = create_new(symbol, faction, email)
    token = response["data"]["token"]

    with open(file_path, "w") as file:
        file.write(token)
    print(f"Token generated in {file_path}")


def get_ship_db_keys():
    response = list_ships()
    if response["meta"]["total"] > response["meta"]["limit"]:
        "f"
    ship_data = response["data"]

    return {key: infer_column_type(value) for (key, value) in ship_data[0].items()}


def infer_column_type(value):
    if isinstance(value, int):
        return "INT"
    elif isinstance(value, str):
        return "VARCHAR(255)"
    elif isinstance(value, dict):
        return "JSONB"
    elif isinstance(value, list):
        return "JSONB"
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")


if __name__ == "__main__":
    data = get_ship_db_keys()
    db_operations.create_table("ship_data", data)
