# Create a program to sum of three number from the user input,
# if user dosn't have any number, use default as 100, 200, 300
from src.ex_08_Functions.Lab069_Function_Types import result

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2 :"))
n3 = int(input("Enter number3 :"))

def sum_of_three_numbers(number1 = 100, number2 = 200, number3 = 300):
    return number1 + number2 + number3

result3 = sum_of_three_numbers(n1,n2,n3)
print("result3", result3)

result4 = sum_of_three_numbers(8,8,8) # without Keyword --> keyword will fetch automatically
print("result4", result4)

result5 = sum_of_three_numbers()
print("result5", result5)

result6 = sum_of_three_numbers(number1 = 10) # passing 1 parameter and other numbers will take from default
print("result6", result6)

result7 = sum_of_three_numbers(number1 = 10, number3=10) # passing 1 parameter and other numbers will take from default
print("result7", result7)

result8 = sum_of_three_numbers(number1=10, number2=20, number3=n3) # number3 will take value from user input because number3 == n3
print("result8", result8)


