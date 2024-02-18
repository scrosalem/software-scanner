from modules.paths import *
import json


class Reader:

    """
    This class is meant to read the JSON files:

    - machines.json
    - apps.json

    Both functions (read_apps and read_machines) are going
    to return a dict type data.

    NOTE: These JSON files are located in the "machines" folder.
    
    """


    @staticmethod
    def read_apps() -> dict:

        with open(apps, encoding='utf8') as f:
            apps_list = json.load(f)

        return apps_list
    

    @staticmethod
    def read_machines() -> dict:

        with open(machines) as f:
            machines_list = json.load(f)
    
        return machines_list
    

    