# User Defined
# 1. They can't return -- non return
# 2. They can return something
# 3. They have Parameters
# 4. They don't have parameters / arguments

# parameters / Arguments = numbers whatever we pass into the function

import math

# Built-in Function
number = max(10,25)
print(number)

# 1. They can't return -- non return
# No return type and no parameter / argument
def greet():
    print("Hello")

greet()

# 2. No return type with argument / parameter

def greet_by_name(name):
    print("Hello", name)

greet_by_name("Rahul")

# 3. No return type and with default Argument (positional argument)

def say_your_name(name = "passing default parameter as Rahul"):
    print("hello, my name is : ", name.upper())

say_your_name("Reddy")
say_your_name()

# 3. Passing multiple arguments with 2 values

def multiple_args(name1="noname" , name2="noname"):
    print("Full name" ,name1 , name2)

multiple_args()
multiple_args(name1 = "Rahul", name2 = "Reddy")
multiple_args(name2 = "Ankith")
multiple_args(name1 = "Sharma")
multiple_args(name2 = "Paul", name1 = "Edmonson")

# 4. Argument + return type

def sum(a,b):
    return a+b

result= sum(3,4)
print("sum of a+b is ", result)

# 4. return type with default parameters

def sum_of_default_values(value1= 10, value2=25):
    return value1 + value2

result1 = sum_of_default_values() # default Parameters
print("Sum of 2 values : ", result1)

result2 = sum_of_default_values(12,30) # call with Parameters
print("Sum of 2 values : ", result2)

