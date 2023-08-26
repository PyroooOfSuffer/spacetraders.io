from urls import *
import logging

logging.basicConfig(filename="log", filemode="w", level=logging.INFO, format="%(levelname)s:%(message)s")


def create_token(symbol, faction, email):
    file_path = "auth_token.txt"
    response = create_new(symbol, faction, email)
    token = response["data"]["token"]

    with open(file_path, "w") as file:
        file.write(token)
    print(f"Token generated in {file_path}")
