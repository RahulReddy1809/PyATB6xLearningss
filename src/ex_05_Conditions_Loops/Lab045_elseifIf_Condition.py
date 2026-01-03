# Find the maximum number between two numbers

num1 = int(input("Enter the num1\n").strip())
num2 = int(input("Enter the num2\n").strip())

if num1 != num2:
    if num1 > num2:
        print("Maximum", num1)
    else:
        print("Maximum", num2)
else:
    print("num1 is equal to num2")