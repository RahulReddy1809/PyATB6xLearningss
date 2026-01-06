# using if-else condition
from random import choice

print("Select the test to run")

print("1. API")
print("2. UI")
print("3. Performance")
print("4. Security")

choice = input("Enter your choice (1:4) : \n" ).strip()

if choice == "1":
    print("we are running POSTMAN API Test case")
elif choice == "2":
    print("we are running SELENIUM UI Test case")
elif choice == "3":
    print("we are running PERFORMANCE Test case")
elif choice == "4":
    print("we are running Security Test case")
else:
    print("Invalid test type")
