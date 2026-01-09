for i in range(0,10,1):
    if i == 5 or i == 6:
        print(i)
    else:
        pass # do nothing- no o/p will be printed

# always draw expression result table (ERT)

# / i / condition / o/p /

# /0 / 0==6 -> False / o/p = "Nothing will be printed"
# /1 / 1==6 -> False / o/p = "Nothing will be printed"
# /2 / 2==6 -> False / o/p = "Nothing will be printed"
# /3 / 3==6 -> False / o/p = "Nothing will be printed"
# /4 / 4==6 -> False / o/p = "Nothing will be printed"
# /5 / 5==5 -> True / o/p = 5
# /6 / 6==6 -> True / o/p = 6
# /7 / 7==6 -> False / o/p = "Nothing will be printed"
# /8 / 8==6 -> False / o/p = "Nothing will be printed"
# /9 / 9==6 -> False / o/p = "Nothing will be printed"

# here, if i ==5 or  i ==6 then only i value will print
# for remaining output will be blank