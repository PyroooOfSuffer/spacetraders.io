import spacetrader_api as api
import os

"""
create_auth_token 
> creates an auth_token for a new account + adds it into auth_token.txt

"""


def create_auth_token(symbol="Pyrooo", faction="COSMIC", email="benjamin.trautweiler.8105@gmail.com"):
    print(f"Your Symbol is {symbol}", f"Your faction is {faction}", f"Your email is {email}")
    confirm = input("Do you want to overwrite the auth_token currently saved? (Y/N): ")
    if confirm.upper() == "Y" or confirm.upper() == "YES":
        response = api.register(symbol, faction, email)
        try:
            auth_token = response["data"]["token"]

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
