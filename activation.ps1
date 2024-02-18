
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
 
netsh advfirewall firewall add rule name="Open Port 139" dir=in action=allow protocol=TCP localport=139

netsh advfirewall firewall add rule name="Open Port 1070" dir=in action=allow protocol=TCP localport=1070

netsh advfirewall firewall add rule name="Open Port 135" dir=in action=allow protocol=TCP localport=135

netsh advfirewall firewall add rule name="Open Port 445" dir=in action=allow protocol=TCP localport=445

netsh advfirewall firewall add rule name="Open Port 69" dir=in action=allow protocol=TCP localport=69

netsh advfirewall firewall add rule name="Open Port 137" dir=in action=allow protocol=TCP localport=137

netsh advfirewall firewall add rule name="Open Port 138" dir=in action=allow protocol=TCP localport=138

netsh firewall set service REMOTEADMIN enable

net start RpcLocator

net start wmiApSrv

net start WinRM 

net start Winmgmt

net start Spooler

net start RpcSs

net start lmhosts

net start SSDPSRV

exit