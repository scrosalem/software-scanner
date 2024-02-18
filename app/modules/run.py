from modules.wm import Connects


class Run:


    @staticmethod
    def check_machines(machines_list, apps, estab) -> None:

        """
		For each computer, it's going to have a connection and scan for every
		software installed, and then generate a txt file with the unwanted ones.

		If it isn't possible to connect to the remote computer, it's going to
		generate a log file.

        NOTE: Read the documentantion (README file) to understand better about
        the "unwanted" softwares mentioned above.
        
        """

        for department, group in machines_list[estab].items():
        
            for host, ip in group.items():

                computer = Connects(ip, host, department, estab, apps)

                connection = computer.remote_connection()

                if connection:
                    computer.get_forbidden_softwares()
                    computer.inspector()
                    computer.generate_txt()

                else:
                    computer.generate_log()


        return
    
    

    