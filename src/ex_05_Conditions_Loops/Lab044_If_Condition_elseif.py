# Find the Positive number is even or odd

number = int(input("Enter the number\n ").strip())

if number >=0:
    if number % 2==0:
        print(f"The entered number {number} is even")
    else:
        print(f"The entered number {number} is odd")
else:
    print(f"the entered number {number} is negative number")


