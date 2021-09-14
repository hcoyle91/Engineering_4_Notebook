# Engineering_4_Notebook
Engineering 4 projects

# Online Python - Dice Roller
import math

import random

print("Automatic dice roller")

input("Press enter to roll:")

print(random.randint(1,6))

check = input("Would you like to roll the dice again? ")

while check == "yes":

    print(random.randint(1,6))

    check =  input("Would you like to roll the dice again? ")

    print(check)

else:
    print("ok goodbye")



