
age = int(input("Enter your age\n ").strip())

if age <= 0 or age > 130:
    print("Enter valid age, age should be from 21 to 130")
else:
    if age >= 21:
        print(f"User age is {age} and eligible to visit club")
    else:
        print(f"User age is {age} not eligible to visit club")
