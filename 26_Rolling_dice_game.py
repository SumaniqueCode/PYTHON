# Created on 2024/03/05
# By Suman Regmi

import random

print("Rolling Dice Game\n------------------")

operation = "y"
while operation == "y" or operation == "Y":
    dice_number = random.randint(1, 6)
    if dice_number == 1:
        print("\n╭━━━━━━━━━╮\n┃         ┃\n┃    ✪    ┃\n┃         ┃\n╰━━━━━━━━━╯")
    elif dice_number == 2:
        print("\n╭━━━━━━━━━╮\n┃         ┃\n┃ ✪     ✪ ┃\n┃         ┃\n╰━━━━━━━━━╯")
    elif dice_number == 3:
        print("\n╭━━━━━━━━━╮\n┃ ✪       ┃\n┃    ✪    ┃\n┃       ✪ ┃\n╰━━━━━━━━━╯")
    if dice_number == 4:
        print("\n╭━━━━━━━━━╮\n┃ ✪     ✪ ┃\n┃         ┃\n┃ ✪     ✪ ┃\n╰━━━━━━━━━╯")
    elif dice_number == 5:
        print("\n╭━━━━━━━━━╮\n┃ ✪     ✪ ┃\n┃    ✪    ┃\n┃ ✪     ✪ ┃\n╰━━━━━━━━━╯")
    elif dice_number == 6:
        print("\n╭━━━━━━━━━╮\n┃ ✪     ✪ ┃\n┃ ✪     ✪ ┃\n┃ ✪     ✪ ┃\n╰━━━━━━━━━╯")

    operation = input("press Y to roll the dice or N to quiet: ")
