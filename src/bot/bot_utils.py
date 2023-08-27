from spacetrader_api import *
#  from ..database import db_operations


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
