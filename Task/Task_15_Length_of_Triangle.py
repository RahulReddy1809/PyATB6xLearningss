# Create a function which will take 3 values from the user, which
# are length of the triangle. side1, side2, side3
# if all sides are equal then, side1==side2==side3 --> Equilateral Triangle
# if any 2 sides are equal then, print --> Isosceles Triangle
# if all sides are different then, print --> Scalene Triangle

def triangle_type():
    side1 = input("Enter side 1 : ")
    side2 = input("Enter side 2 : ")
    side3 = input("Enter side 3 : ")

    if side1 == side2 == side3:
        print("Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

triangle_type()
