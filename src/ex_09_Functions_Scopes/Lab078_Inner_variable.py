def outer_function():
    var1 = 30

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function1():
        print(var1)

    inner_function() # Calling inner function
    inner_function1() # Calling inner function

outer_function() # # Calling outer function