import database as db
import spacetrader_api as api
import os


def create_auth_token(symbol="Pyrooo", faction="COSMIC", email="benjamin.trautweiler.8105@gmail.com"):
    confirm = input("Do you want to overwrite the auth_token currently saved? (Y/N): ")
    if confirm.upper() == "Y" or confirm.upper() == "YES":
        response = api.register(symbol, faction, email)
        try:
            auth_token = response["token"]

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "auth_token.txt")

            with open(file_path, "w") as file:
                file.write(auth_token)

            print("Auth token has been successfully updated and saved to auth_token.txt")

        except Exception as e:
            print("Error while getting new Auth_Token", e)
            print("API Response: ", response)
    else:
        print("Creating a new auth_token aborted")


def flatten_dict(data_dict, parent_key='', sep='_'):
    flattened = {}
    for key, value in data_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, sep=sep))
        else:
            flattened[new_key] = value
    return flattened


def create_column_type(flattened_data):
    column_type = ", ".join([f"{key} {type_name}" for key, type_name in flattened_data.items()])
    return column_type


def create_column_data(flattened_data):
    column_value = {}
    for key, value in flattened_data.items():
        parts = key.split('_')
        if len(parts) > 1:
            index, field_name = parts[-2], parts[-1]
            if index not in column_value:
                column_value[index] = {}
            column_value[index][field_name] = value
        else:
            column_value[key] = value
    column_value = list(column_value.values())
    return column_value


db.create_table("space", "ships", "f")
