#!/usr/bin/env python
import socket
import subprocess
import sys
import os
import time
from datetime import datetime
import platform

#colors
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
white = "\033[1;37;40m"

#asks user for input
target = input("Please enter the host to scan: \n")
try:
    targetIP = socket.gethostbyname(target)

except:
    print("invalid host RETURNING")
    os.system("python3 Poisonivy.py")

#asks the user the range of ports to scan
portRange1 = int(input("Scan from port : \n"))
portRange2 = int(input("to port : \n"))
time.sleep(1)
print(f"You have chosen to scan from port {portRange1} - {portRange2}\n")

#separates with a sort of banner
print("-" * 75)

print(f"Scanning the target of : {targetIP}")
print("_" * 75)

#time started scan
time1 = datetime.now()

try:
    for i in range(portRange1,portRange2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((targetIP, i))
        print(f"Scanning port {i}")
        if result == 0:
            print(f"Port {i}:   Open\n")
        s.close()

except KeyboardInterrupt:
    print("\nQUITTING.......")
    sys.exit()
except socket.gaierror:
    print("Host could not be resolved: \n QUITTING.......")
    sys.exit()
except socket.error:
    print("Connection not met: \n QUITTING.......")
    sys.exit()

#checks time after scan
time2 = datetime.now()

totalTime = time2 - time1

print("-" * 75)

print(f"Full scan completed in :{totalTime}")
time.sleep(1)
print(blue + "Returning to menu:\n")
time.sleep(3)
os.system("python3 Poisonivy.py")