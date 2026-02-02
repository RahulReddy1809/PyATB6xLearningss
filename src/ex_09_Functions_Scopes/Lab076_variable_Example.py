public_toilet = "Public"

def home():
    private_toilet = "Private"
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet) # This variable can be accessed by any function
    # print(private_toilet) -> this will not print as it is private variable for only home() function

home()
stranger()