
"""
path.py is responsible for setup the files paths so you don't have to worry about
manipulate it manually.

The reason for that, is if you realocate the project to another location, you would
have to change all the paths manually.

This way (with pathlib) it doesn't matter where you store the project, it'll always
find the important files, such as:

- machines.json
- apps.json
- "result" folder
- "logs" folder
        
"""


# Importing library to manipulate paths
import pathlib

# Path to main folder.
repo = pathlib.Path(__file__).parent.absolute().parent.parent


# Storing the files paths.
machines = repo / 'machines' / 'machines.json'

logs = repo / 'logs' / 'logs.txt'

apps = repo / 'machines' / 'apps.json'

result_folder = repo / 'results'
