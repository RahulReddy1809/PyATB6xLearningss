# Given a number, you need to calculate the factorial of that number
import math

n = 5           # number to find factorial
fact = 1        # Variable to store factorial

for i in range(1,6):
    fact = fact * i
print("Factorial of", n, "is", fact)

