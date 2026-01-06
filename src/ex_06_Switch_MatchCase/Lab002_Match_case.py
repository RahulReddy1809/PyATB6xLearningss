print("Enter which test you want to run")
test_type = input("Enter the Test Type : API, UI, Performance, Security \n")

# default condition(underscore _) should be written at the ned of the code

match test_type :
    case "API":
        print("we are running POSTMAN API Test case")
    case "UI":
        print("we are running SELENIUM UI Test case")
    case "Performance":
        print("we are running PERFORMANCE Test case")
    case "Security":
        print("we are running Security Test case")
    case _:
        print("Invalid test type")
