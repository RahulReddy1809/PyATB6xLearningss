def display_information(name, role):
    print(f"Your name is {name}, and his role is {role}")

display_information("Rahul", "QA") # passing values at the time function calling
display_information(name = "Rahul", role ="QA2") # Passing Keyword argument
display_information(role ="QA3", name = "Rahul") # inter-changing parameters also possible

