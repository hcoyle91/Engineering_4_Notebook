import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def doMath(a,b,c):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        return a / b
    elif c == 5:
        return a % b
    
print("Sum:\t\t" + str(doMath(a,b,1)))
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))

