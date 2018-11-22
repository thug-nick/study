
#!/usr/bin/python3

import telnetlib
import sys
import getpass
import ipaddress

HOST = "cisco-ip.here"
USER = "asker"
PASSWORD = "1"


try:
	ipaddr = input("Enter IP: ")
	checkip = ipaddress.ip_address(ipaddr)
except ValueError:
	print ("ip error")
	sys.exit(1)

print(checkip)
