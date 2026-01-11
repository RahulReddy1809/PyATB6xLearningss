# Function within the function --> Nested Function

def f1(): # declaring outside
    print("Hi")
    def f2(): # declaring inside
        print("Welcome to functions")
    f2() # Calling inside function
f1() # Calling outside function