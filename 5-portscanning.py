#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target.
if len(sys.argv) == 2: # Check if we have at least 2 command line arguments. 
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()
	
# ADD A PRETTY BANNER
print('.'*75)
print(f' Scanning Target: {target}')
print(f' Time Started: {datetime.now()}')
print('.'*75) 		
	
try: 
	for port in range(1, 65535):
		# A TCP CONNECTION
		socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.2) # Set a default time-out of .2 seconds 
		result = socket_connection.connect_ex((target, port)) #Connects to the target:port,and returns 0 on success and 1 on error
		if result == 0:
			print(f' Port {port} of {target} is open')
		socket_connection.close() 
except KeyboardInterrupt:
	print("\n Exiting Program.")
	sys.exit() 
	
except socket.gaierror:
	print("Hostname {sys.argv[1]} could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")	
	sys.exit()			
				