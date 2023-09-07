import console as c

"""
venv - not on GitHub -   - not code -
> virtual environment for PyCharm

.gitignore  - not code -
> which files to not update on GitHub

auth_token.txt - not on GitHub -  - not code -
> the token as a single string

bot.py
> automate some process (for starters update all ships +  my_agent + current system/waypoints?)
>> data transforming for db here or in database.py?? or create updater.py?
>> create a universal function to read out date of any response? or add every response from hand?

console.py
> allow control of the program over console (currently able to use spacetrader_api func)

database.py (needed? cant hust define/update global dicts?)
> create and manage the database and table
>> data transforming for db here or in bot.py?? or create updater.py?
>> create a universal function to read out date of any response? or add every response from hand?

main.py
> calls all function

requirements.txt - not code -
> all requirements so PyCharm gets all imports

spacetrader_api.py - no change needed -
> all requests to API as functions
"""

if __name__ == "__main__":
    c.console()
