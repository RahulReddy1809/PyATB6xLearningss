# Create a function which will take a positive number from the user
# and perform a square of the number

def square_of_numbers():
    number = float(input("Enter a positive number : "))

    if number > 0:
        square = number**2
        print("Square of the number is : ", square)
    else:
        print("Please enter a positive number")
square_of_numbers()
