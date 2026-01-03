# Find the Maximum between 3 numbers

# Logic Building

# User Inputs : num1, num2, num3
# User Output : provides Max number

num1 = int(input("Enter num1\n ").strip())
num2 = int(input("Enter num2\n ").strip())
num3 = int(input("Enter num3\n ").strip())

if num1 >= num2 and num1 >= num3:
    print("Maximum is num1", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maximum is num2", num2)
else:
    print("Maximum is num3", num3)