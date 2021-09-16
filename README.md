# Engineering_4_Notebook
## Table of contents
* [Table Of contents](table-Of-Contents)
* [Python Code](Python-Code)

## Python code
### Dice roller
```C
import random                           # import the library random so I can determine a random number
print("Automatic dice roller")          # Says the title in terminal
diceSides = int(input("how many side should the dice have? "))                      # Declares diceSides as the input from that question and casts that input as an int
numDice = int(input("How many dice should there be? "))                             #Declares numDice as the the input from that question and casts it as an int
input("Press enter to roll:") #First roll
for i in range (0,numDice):                                 #Goes through the folllowing actions for every integer from 0 to whatever numdice was inputed as
    print(random.randint(1,diceSides))                      #Prints a random number with in the data set from 1 to whatever dicesidesis according to the input

check = input("Would you like to roll the dice again? ")    #Defines check as an input string

while check == "yes":                                        # creates a loop that occurs while the variable check is inputed as yes
    for x in range(0,numDice):                               #Same as above
        print(random.randint(1,diceSides))
    check =  input("Would you like to roll the dice again? ")
  

else:                                                       # If the variable check is not equal to yes then it will execute the following actions
    print("ok goodbye")
```
### Calculator
```c
import math
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))


difference = firstNum - secondNum
sum1 = firstNum + secondNum
product = firstNum * secondNum
quotient = firstNum / secondNum
modulo = firstNum % secondNum
print("The difference: "+str(difference)+" The sum: "+str(sum1)+" The product: "+str(product)+" The quotient: "+str(quotient)+" The modulo: "+str(modulo))
```
