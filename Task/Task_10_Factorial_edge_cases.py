
num = int(input("Enter for which number you need factorial : "))

fact = 1

if fact <0:
    print("Factorial is not defined")

if fact == 0:
    print("FACT", fact)
else:
    for i in range(1,num+1):
        fact = fact * i
print(f"Factorial of {num} is ", fact)