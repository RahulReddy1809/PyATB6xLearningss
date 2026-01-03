# We can also write in one-liner condition by using ternary operator

number = int(input("Enter the number\n ").strip())

if number >= 0:
    print("Even number" if number %2 == 0 else "Odd number")
else:
    print("Negative number")
