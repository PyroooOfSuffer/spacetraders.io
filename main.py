import console as c
import simple_automation as sa
import spacetrader_api as api

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

main.py
> calls all function

prototype_data.py 
> a prototype file with the right data

requirements.txt - not code -
> all requirements so PyCharm gets all imports

simple_automation.py
> some easy automation, currently contains:
>> generate a token + write into auth_token.txt
>> flatten dicts
>> create column_type for the create_table in database.py
>> create column_data for the add_data in database.py

spacetrader_api.py - no change needed -
> all requests to API as functions
"""

if __name__ == "__main__":
    print(prototype_navigation.denest_dict(prototype_data.ship_list_data[0]))
