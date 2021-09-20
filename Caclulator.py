
import math                                     ## imports the math library
a = int(input("Enter the first number: "))      ## takes the first number inputed as an int called a
b = int(input("Enter the second number: "))     ## takes the second number input aas an int called b

def doMath(a,b,c):                   # Defines the a new function as 'doMath' that takes three inputs a b and c
    if c == 1:
        return a + b                    # Within the function, if c is 1 output the sum of a and b
    elif c == 2:
        return a - b                    # does the same thing but for a different c and a differnet output
    elif c == 3:
        return a * b                        # does the same thing but for a different c and a differnet output
    elif c == 4:
        return a / b
    elif c == 5:
        return a % b
    
print("Sum:\t\t" + str(doMath(a,b,1)))          # Calls the function doMath and prints it for when c=1. the /t/t is just for formating. This code does that for c from 1 to 5
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
