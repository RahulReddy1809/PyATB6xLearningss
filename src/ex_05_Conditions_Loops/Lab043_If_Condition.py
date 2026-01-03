# write a program to take a user age and
# let him know if he can go to club.
# age is > 21

# Logic Building Formula
# step 1
# i/p : age, int
# o/p : can go to clud or not

#step 2 : Rough Logic
"""
age > 21 "can go to club"
age < 21 "cannot go to club"
"""
# Step 3: write the logic


age = int(input("Enter your age : "))

if age >= 21:
    print(f"User age is {age} and he can visit the club ")
else:
    print(f"User age is less than 21, not eligible to visit club")

# Step 4: Check for the edge cases.
# we should consider edge cases as :
# Negative ages or extremely high values -> program will break
# Non-numeric input - ABC
# Age which is valid > 130

# Step 5 : Optimize the code.
# Handle all the edges.

