# FizzBuzz test

# write a program that prints numbers from 1 to 100. however, for multiples of 3,
# print "Fizz", for multiples of 5, print "Buzz". For numbers that are multiple
# of both 3 and 5, print "FizzBuzz".

# program brief
# For multiples of 3, print "Fizz"
# For multiples of 5, print "Buzz"
# For multiples of 3 and 5, print "FizzBuzz"

# num = int(input("Enter any number form 1 to 100 : "))
for i in range(1,101):
    if i % 3==0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)




