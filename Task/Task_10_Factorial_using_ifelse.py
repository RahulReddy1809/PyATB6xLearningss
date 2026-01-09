num = int(input("Enter the number for which you need factorial : "))

fact = 1

if num <= 0:
    print("Fact = ", fact)
else:
    for i in range (1,num+1):
        fact = fact *i
print(f"Factorial of {num}: ", fact)