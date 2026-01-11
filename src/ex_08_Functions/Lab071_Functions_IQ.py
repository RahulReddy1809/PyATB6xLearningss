
def sum_three(a=1, b=1,c=1):
    return a+b+c

result_one = sum_three()
print(result_one)

result_two =sum_three(1,2)
print(result_two)

result_three = sum_three(1,2,3)
print(result_three)

result_four = sum_three(b=67, a=10, c=45)
print(result_four)

result_five = sum_three(a=10, b=67, c=45)
print(result_five)

