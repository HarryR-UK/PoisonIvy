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

print(white + "")
#clears screen
#if platform.system() == "Windows":
    #subprocess.call('cls', shell=True)
#else:
    #subprocess.call('clear', shell=True)

#title card
print("A program created by : \n")
print ("""
 ____   ___  ____ _____  ___   ____   ____  __ __  __ __ 
|    \ /   \|    / ___/ /   \ |    \ |    ||  |  ||  |  |
|  o  )     ||  (   \_ |     ||  _  | |  | |  |  ||  |  |
|   _/|  O  ||  |\__  ||  O  ||  |  | |  | |  |  ||  ~  |
|  |  |     ||  |/  \ ||     ||  |  | |  | |  :  ||___, |
|  |  |     ||  |\    ||     ||  |  | |  |  \   / |     |
|__|   \___/|____|\___| \___/ |__|__||____|  \_/  |____/ 
                                                         

                 -- HR""")
time.sleep(1)
print("-" * 75)
time.sleep(1)
print("""
      DISCLAIMER:

      This project does some stuff which may violate privacy, or even destroy your own computer (RUSSIAN ROULETTE),
      Please use this program at your own risk.
      """)
time.sleep(1)
print("-" * 75)
time.sleep(1)
programSelection = 0

# the different options for the program
programSelection = 0
programSelection = int(input(red + """Please choose which program to use: \n 
[1] - URL to IP address  
[2] - Port Scanner  
[3] - Spam Bot
[4] - Russian Roulette (not recommended) 
[5] - Brute force attack 
[6] - Ping an IP
[7] - Encrypt a file

"""))

print(white + "")

#url converter
if programSelection == 1:
    os.system("python3 Programs/Poisonivy_URL_To_IP.py")
#port scanner
elif programSelection == 2:
    os.system("python3 Programs/Poisonivy_port_Scanner.py")
#spammer
elif programSelection == 3:
    os.system("cd Programs/SpamBot && python3 SpamBot.py")
#russian roulette
elif programSelection == 4:
    os.system("python3 Programs/Poisonivy_Russian_Roulette.py")
#brute force
elif programSelection == 5:
    print("STILL IN PROGRESS...sorry")
elif programSelection == 6:
    os.system("python3 Poisonivy_ping.py")
elif programSelection == 7:
    print("STILL IN PROGRESS...sorry")
else:
    print(white + "Entered value was out of range of the given values, please enter the given numbers:\n")
    
