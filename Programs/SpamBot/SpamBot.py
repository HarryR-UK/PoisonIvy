import pyautogui, time
import os

#colors
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
white = "\033[1;37;40m"



choice = int(input("\033[1;33;40mWould you like to use an external file or type the spam words now? (1 for file, 2 for choice)\n"))

if choice == 2:
    spamText = input("\033[1;36;40mEnter the text to spam: \n")
elif choice == 1:
    openFileInput = input("Enter the name of the file you wish to spam (you want to make sure the file is in the same folder as this scipt)\n")
    file = open(openFileInput, "r")
    lines = file.read()
    spamText = lines
else:
    print("number chosen not in range of expected values....EXITTING \n")
    exit()

time.sleep(0.5)

infiniteLoop = int(input("Would you like the spam to be infinite or a fixed value (1 for infinite 2 for fixed)\n"))

time.sleep(0.5)

if infiniteLoop == 2:
    range = int(input("\033[1;36;40mHow many times would you like to repeat the spam? \n"))
    timeBeforeSpam = float(input("\033[1;31;40mAfter this text the spam will start, to give you time to get ready, how long would you like (in seconds) top wait until the spam starts?\n"))
    time.sleep(timeBeforeSpam)
    i = 0
    while i < range :
        pyautogui.typewrite(spamText)
        pyautogui.press('enter')
        i +=1
elif infiniteLoop == 1:
    timeBeforeSpam = float(input("\033[1;31;40mAfter this text the spam will start, to give you time to get ready, how long would you like (in seconds) top wait until the spam starts?\n"))
    time.sleep(timeBeforeSpam)
    while True:
        pyautogui.typewrite(spamText)
        pyautogui.press('enter')
else:
    print("number chosen not in range of expected values....EXITTING \n")
    exit()

if choice == 1:
    file.close()
print("\033[1;33;40mI hope your targer is annoyed! :P")
print(blue + "RETURNING TO MENU....")
time.sleep(2)
os.system("python3 Poisonivy.py")
