# Given a number, you need to calculate the factorial of that number

# range = (start, stop, step)
# range = (stating number, n-1, difference between numbers)

n = int(input("Enter a number for which you need factorial for :"))   # number to find factorial
fact = 1        # Variable to store factorial

for i in range(1,n+1): # n+1 gives the exact range till n, becoz stop = n-1
    fact = fact * i
print(f"Factorial of {n}", "is", fact)

