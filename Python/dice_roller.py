import random ## imports a library random

print("Automatic Dice Roller") ## prints the title 

value="" ## initializes the variable value as " "

while value == "":   # because value is already set as "" the while loop begins
    randomNum = random.randint(1, 6) ## set randomnum to 
    value = input("Press Enter to roll, press x then Enter to quit") ## takes an input
    
    if value == "":  ## if user hits enter, it will take the randomnum (already set to a random integer) and print it
        print(randomNum)
        print("Roll the dice again?")
    else:
        print("Ok, Goodbye") ## if the user types anything else, say good bye
    
