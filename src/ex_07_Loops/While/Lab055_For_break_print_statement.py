for i in range(0,10): # 0 to 9 --> 10times

    if i ==5:
        break
    print(i)

# here, print statement will work till i == 4 and then it will break

# always draw expression result table (ERT)

# / i / condition / o/p /

# /0 / 0==5 -> False / o/p = 0
# /1 / 1==5 -> False / o/p = 1
# /2 / 2==5 -> False / o/p = 2
# /3 / 3==5 -> False / o/p = 3
# /4 / 4==5 -> False / o/p = 4 and then break out of for Loop

# Here, program will print till 4 because print(i) is updated after break statement
# program will execute until the loop i == 4, and then it will break
# remaining numbers will not print