# Engineering_4_Notebook

import random # import the library random so I can determine a random number
print("Automatic dice roller") # Says the title in terminal
diceSides = int(input("how many side should the dice have? ")) # Declares diceSides as the input from that question and casts that input as an int
numDice = int(input("How many dice should there be? ")) #Declares numDice as the the input from that question and casts it as an int
input("Press enter to roll:") #First roll
for i in range (0,numDice): #Goes through the folllowing actions for every integer from 0 to whatever numdice was inputed as
    print(random.randint(1,diceSides)) #Prints a random number with in the data set from 1 to whatever dicesidesis according to the input

check = input("Would you like to roll the dice again? ") #Defines check as an input string

while check == "yes": # creates a loop that occurs while the variable check is inputed as yes
    for x in range(0,numDice):   #Same as above
        print(random.randint(1,diceSides))
    check =  input("Would you like to roll the dice again? ")
  

else:  # If the variable check is not equal to yes then it will execute the following actions
    print("ok goodbye")


    ```


