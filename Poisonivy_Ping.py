import subprocess
import os 
import time

#colors
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
white = "\033[1;37;40m"



ipAddress = int(input(purple + "Please choose what IP address you would like to ping, or type `EXIT` to quit the program: \n"))
if ipAddress == 'EXIT':
    time.sleep(1)
    print(red + "Returning......")
    time.sleep(0.5)
    os.system("python3 Poisonivy.py")
else:
    try:
        test = subprocess.Popen(["ping", ipAddress])     
        output = test.communicate()[0]
    except KeyboardInterrupt:
        print(yellow+"STOPPING!")
        time.sleep(1)
        print(blue+ "Returning.....")
        time.sleep(0.5)
        os.system("python3 Poisonivy.py")






