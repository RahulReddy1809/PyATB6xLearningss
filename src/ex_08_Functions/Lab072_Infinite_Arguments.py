# how to add infinite arguments / Parameters

def multiple_arguments(*multplearguments): # here * indicates can enter multiple parameters as below
# arguments -> will pass the values in the form of list - list will allow all data types
    for i in multplearguments:
        print(i)

multiple_arguments("Rahul")
multiple_arguments("Sardar", "Reddy")
multiple_arguments("Rahul", "Nation", 31.33)
multiple_arguments("Rahul", "Animal", 42, "Tiger")
