def greet_with_default_parameter(name = "Default parameter"):
    print("Hi", name )

greet_with_default_parameter("Rahul") # if parameter is given while calling function - will consider it
greet_with_default_parameter("Reddy")     # if no parameter given while calling the function - will take default parameter whichever is defined
greet_with_default_parameter()