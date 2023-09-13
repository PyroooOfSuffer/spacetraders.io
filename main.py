import console as c
import simple_automation as sa
import spacetrader_api as api
import requests

"""
venv - not on GitHub -   - not code -
> virtual environment for PyCharm

xold - folder - 
>> contains usable files that i dont need for the current interation of the program

.gitignore  - not code -
> which files to not update on GitHub

auth_token.txt - not on GitHub -  - not code -
> the token as a single string

console.py
> allow control of the program over console (currently able to use spacetrader_api func)

main.py
> calls all function

prototype_data.py 
> a prototype file with the right data

requirements.txt - not code -
> all requirements so PyCharm gets all imports

simple_automation.py
> some easy automation, currently contains:
>> generate a token + write into auth_token.txt

spacetrader_api.py - no change needed -
> all requests to API as functions
"""

if __name__ == "__main__":
    print("send Help")
    print(api.get_status())
