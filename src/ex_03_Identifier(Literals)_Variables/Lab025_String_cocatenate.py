"""
concatenate between 2 strings are allowed
concatenate between 2 integer are allowed
but
concatenate between str and int are not allowed unless both should be same datatype
if not we have to convert them into same datatype.

In-compatable datatype - which are different datatypes

"""

name = "this is a big sentence"
print(type(name))

new_name = name + " " + str(15)
print(new_name)
print(type(new_name))

first_name = "Rahul"
last_name = "Reddy"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

