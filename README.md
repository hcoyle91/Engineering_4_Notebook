# Engineering_4_Notebook
Engineering 4 projects
##Table of contents:
* [Table of contents](#Table-of-contents)
* [Hello Python](#Hello-Python)


## Hello Python
```C

import math
import random
print("Automatic dice roller")
diceSides = int(input("how many side should the dice have? "))
numDice = int(input("How many dice should there be? "))
input("Press enter to roll:")
for i in range (0,numDice):
    print(random.randint(1,diceSides))

check = input("Would you like to roll the dice again? ")

while check == "yes":
    for x in range(0,numDice):
        print(random.randint(1,diceSides))
    check =  input("Would you like to roll the dice again? ")
  

else:
    print("ok goodbye")
    ```


