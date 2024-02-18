<h1 align="left">Python - WMI Software Scanner</h1>

## 📝 Introduction - About the Project
*Python - WMI Software Scanner* is a project created to scan all softwares installed on the network, **filtering** for those that **should not be installed.**

**Example scenario:**
You work at a company that has 200 employees. In this company, there's a list of softwares that all computers must have. You need to check if any user has installed an extra software (for instance, a bank application your boss told you it's not allowed).

With *WMI tool* you can scan for all softwares installed on every computer. <br>
With *Python*, you can **automate it.**


#

**NOTE:** This project only works for **WINDOWS** (since WMI is a Microsoft's management tool). So this project is built for this specific environment.

#
<h3>Requirements</h3>

* `Python 3.9` (More specific 3.9.10) - Other versions have not been tested.
* `Windows 10` (Host and Client) - Other versions (Windows 7 and Windows 11) have not been tested.




## 📌 WMI - Description 
Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on **Windows-based operating systems**.

WMI provides users with information about the status of local or **remote computer systems** and supports the following actions:

* Configuring security settings.
* Setting and changing system properties.
* Setting and changing permissions for authorized users and user groups.
* Assigning and changing drive labels.
* Scheduling processes to run at specific times.
* Backing up the object repository.
* Enabling or disabling error logging.


For this **project's purpose**, we are going to use it to connect on a remote computer and **scan for the inappropriate softwares**

## ✅ Setup the Environment

To use WMI tool, you must have **RPC (Remote Procedure Call)** service running on the *client* (computer you are going to scan) and on the *server* (host computer running the script). You also need to start more services and **open a few ports on the firewall** to be able to make **remote connections.**


To simplify all these operations, there's a powershell script called `activation.ps1`  where all services needed are activated and all firewall's ports necessary are open. Run this script with **admin privileges.**

Yes, you need to run this powershell script on **every computer** that you want to scan.

#
⚠️ **DISCLAIMER:** Run services and open firewall ports may impact your network security issues. Do it only if you know what you're doing, or contact you network's administrator to understand better.
#


## 📑⚙️ Setup JSON File - Machines
In ```machines.json``` you can **add** all the computers that you want to connect and scan for installed softwares.

This entire project was built to work with this **json structure:**

```
{
    "ESTABLISHMENT-1": {

            "DEPARTAMENT-1": {
                "COMPUTER-1": "192.168.0.12",
                "COMPUTER-2": "192.168.0.13",
                "COMPUTER-3": "192.168.0.14"
            },

            "DEPARTAMENT-2": {
                "COMPUTER-1": "192.168.0.15",
                "COMPUTER-2": "192.168.0.16",
                "COMPUTER-3": "192.168.0.17"
            }
    }

}
```


**NOTE:** You can restructure this to fit in your case, but you'll have to change the code to work with your model.



## 📑⚙️ Setup JSON File - Apps
In the example scenario (introduction section), i said about a list of softwares that all computers must have.

Well, you'll add these softwares in ```apps.json```

```
{

"commons": [
    "Google Chrome", "7-Zip", "WinRAR", "Java",
    "TeamViewer", "Foxit Reader", "AnyDesk",
    "Windows Live Essentials", "Realtek Audio COM Components",
    "HP Update", "Realtek High Definition Audio Driver"
]

}
```
**NOTE:** You can restructure this to fit in your case, but you'll have to change the code to work with your model.

In "commons", i put all the softwares that every computer must have. This means that when we run the script, it's going to compare the softwares on the list with the softwares found on the remote computer. The softwares (found on the remote computer) that **ARE NOT** on the list, is going to be written into a TXT file.

For instance, i have a computer containing:
* Google Chrome
* TeamViewer
* Bank Application

The `Google Chrome` and `TeamViewer` are added in the `app.json`, but the `Bank Application` is not. That means when i run the script, it'll return only the `Bank Application`, meaning that software should not be installed on that computer.  

## ✅ Setup - Host and Client
**SETUP HOST** <BR>
Cloning the repository
```
git clone https://github.com/scrosalem/software-scanner.git
```

Open ->   **.\software-scanner\app** and create a virtual venv
```
python -m venv venv

.\env\Scripts\activate
```
Install the requirements 
```
pip install -r .\requirements.txt
```

Running the script
```
python main.py
```

#
**SETUP CLIENT** <BR>
You need to run the powershell script `activation.ps1` on the client computer to be able to connect. **Run it as admin privileges.**

## 🗝️ Conclusion
I know there are other tools (Zabbix is one example) that can do the same thing (and even better), but at the time i didn't have other options, so i had to create my own. Python and WMI were my solution.

Certainly there's a lot to be improved in this project, but i think this is a good start.

#

Better explanation about the WMI tool:
* https://www.techtarget.com/searchenterprisedesktop/definition/Windows-Management-Instrumentation-Command-line-WMIC#:~:text=The%20Windows%20Management%20Instrumentation%20Command%2Dline%20(WMIC)%20utility%20is,operations%20on%20a%20Windows%20computer.

<br>

What else you can do with Python and WMI:
* https://timgolden.me.uk/python/wmi/tutorial.html

<br>

Download Python 3.9:
* https://www.python.org/downloads/release/python-3910/