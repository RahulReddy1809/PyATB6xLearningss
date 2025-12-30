# write a python program to calculate the
# area of circle given its radius using the formula
# ''' area = pie * r ^2 (take pie as = 3.14)

# i/p --> r - float
# 0/p --> string formated output of area

radius = float(input("Enter radius of a circle : "))
area_of_circle = 3.149876*radius **2
print("Area of circle is -> " , area_of_circle)
# F strings - formated string --> string data formating
print(f"Area of circle is -> {area_of_circle:.2f}")
