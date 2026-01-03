# Grade calculator:

# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g A, B, C, D, F)
# based on the following grading scale

# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 0 -59

score = int(input("Enter the score\n :").strip())

if score > 100 or score < 0:
    print("Enter Valid Score")
else:
    if score >=90 and score <= 100:
        print("Your Grade is A")
    elif score >= 80 and score <= 89:
        print("Your Grade is B")
    elif score >= 70 and score <= 79:
        print("Your Grade is C")
    elif score >= 69 and score <= 60:
        print("Your Grade is D")
    else:
        print("Your Grade is F")





