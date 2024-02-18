from modules.run import Run
from modules.reader import Reader


def run_machines() -> None:

    """
    Here is where everything begins.

    The JSON files (machines.json and apps.json) need to be configured.

    NOTE 1: Depending on how you configure the JSON files (ex: if you change
    the JSON structure), you'll need to adapt this script to work with those
    settings.

    NOTE 2: Read the documentation on the GitHub (README file) to understand
    better about this project and how to configure properly.
    
    """


    estab = ["ESTABLISHMENT-1", "ESTABLISHMENT-2"]


    machines_list = Reader.read_machines()
    apps_list = Reader.read_apps()



    # Importing this to scan more than 1 estab at the same time.
    import multiprocessing


    m0 = multiprocessing.Process(
        target=Run.check_machines,
        args=(machines_list, apps_list, estab[0]))
    
    

    m1 = multiprocessing.Process(
        target=Run.check_machines,
        args=(machines_list, apps_list, estab[1]))
    

    m0.start()
    m1.start()
    
    return



