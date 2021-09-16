import random

print("Automatic Dice Roller")

value="" 

while value == "":
    randomNum = random.randint(1, 6) 
    value = input("Press Enter to roll, press x then Enter to quit")
    
    if value == "": 
        print(randomNum)
        print("Roll the dice again?")
    else:
        print("Ok, Goodbye")
    
