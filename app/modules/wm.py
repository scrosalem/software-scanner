# Importing the WMI library. 
import wmi

# Importing the path to JSON files.
from modules.paths import *

# Importing the libraries to datetime functions.
from datetime import date
import time



class Connects:

    """
    This class uses the WMI (Windows Management Instrumentation) library.
		
    WMI is a native tool installed on Windows. It's meant to do administrative
    tasks in remote computers, such as looking what kind of softwares are installed,
    which is the main purpose here.


	NOTE: The RPC (Remote Proceduce Call) service needs to be running in both
	computers (client and server) to make the WMI tool work. If you need more
    details on how to do it, there is a explanation in the project's documentation.

    """


    def __init__(self, ip, host, department, estab, apps):

        """
        CONSTRUCTOR
				

        * Windows Credentials. -> The account must have admin privileges. Otherwise, it won't connect
		to the remote computer.
        self.username        -> remote computer's admin user account. *Windows Credentials.
		self.password        -> remote computer's admin password. *Windows Credentials.

        
		self.softwares       -> All the unwanted softwares are going to be stored here.
		self.apps            -> All the allowed softwares are going to be stored here.

		self.judge           -> True = It was found unwanted softwares in the remote computer.
								False = All good, there's no forbidden softwares in the remote computer.
        
        """

        self.ip=ip
        self.host=host
        self.department=department
        self.estab=estab
        self.apps = apps
        self.username='username'
        self.password='password'
        self.softwares = []
        self.judge = bool
        


    def remote_connection(self) -> bool:

        """ 
        This function is responsible to create the connection
        to the remote computer.

        If the connection is made, it returns it.
        But if there's no connection, it returns False.

        """

        try:
            print(f'Establishing connection to {self.host} ({self.ip})')

            self.connection = wmi.WMI(
                self.ip,
                user=fr'{self.ip}\{self.username}',
                password=self.password
                )

            print (f"Connection established to {self.host} ({self.ip})")
            return self.connection

        except wmi.x_wmi:
            print (f"Failed to connect to {self.host} ({self.ip})")
            self.connection = False
            return self.connection
        


    def get_forbidden_softwares(self) -> list:

        """ 
        This function is going to collect all softwares installed on the
        remote computer, and store them in the variable self.softwares

        After that, it's going to compare the self.softwares, with the
        softwares in self.apps's list.

        Then, it'll return the softwares that are not in the self.apps's list.

        """

        try:
            for info in self.connection.Win32_InstalledWin32Program():
                app_name = str(info.Name).encode('utf8','ignore').decode()

                if app_name not in self.softwares:
                    self.softwares.append(app_name)

                for app in self.apps["commons"]:
                    if app in app_name:
                        self.softwares.remove(app_name)
        except:
            pass
            
        return self.softwares



    def generate_log(self) -> None:

        """
        In case the connection to the remote computer fail, then it's going to
        generate a log, containing the computer's name, ip and datetime that
        occured the scan.

        """

        day = self.get_date()
        time = self.get_time()

        error_message = f'Failed to connect to "{self.host}" ({self.ip}) - Day: {day} - Time: {time}\n'

        print(f'-> Generating log on {self.host} ({self.ip})...')
        with open(logs, 'a') as f:
            f.write(f'{error_message}\n')

        return



    def inspector(self) -> bool:

        """
        If the scanner found some softwares, it returns True.

        If the scanner didn't find some softwares, then it
        returns False.

        """

        num = len(self.softwares)

        if num == 0:
            self.judge = False
            return self.judge

        else:
            self.judge = True
            return self.judge



    def generate_txt(self) -> None:
        
        """
        This function is going to create a txt file with all
        the softwares that were found while scanning the computer.

        """

        if self.judge == True:

            with open(f'{result_folder}\{self.host} ({self.ip}).txt',
                 'w', encoding='utf-8') as f:

                for software in self.softwares:
                    f.write(f'{software}\n')

        else:
            pass

        return
    


    def get_date(self) -> str:

        """
        This function returns the current date.
        
        """

        today = date.today()
        current_date = today.strftime("%d/%m/%Y")
        
        return current_date



    def get_time(self) -> str:

        """
        This function return the current time.
        
        """

        current_time = time.strftime("%H:%M")
        return current_time

