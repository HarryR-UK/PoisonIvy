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

url = ""


url = input(purple + "Please enter the url/website you wish to resolve (for example www.google.com): \n")


try:
    urlIp = socket.gethostbyname(url)
    print(yellow + f"The IP of the entered url is :\n {urlIp}")
    time.sleep(1)
    print("Returning to menu: \n")
    time.sleep(3)
    os.system("python3 Poisonivy.py")
except:
    print("invalid url\n")
    time.sleep(1)
    print("returning.....")
    time.sleep(2)
    os.system("python3 Poisonivy.py")


