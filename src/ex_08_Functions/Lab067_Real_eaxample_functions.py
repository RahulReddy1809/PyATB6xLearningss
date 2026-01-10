def validation_of_status_code(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Error in the Request")
validation_of_status_code(200)
validation_of_status_code(404)
validation_of_status_code(response_code=200)
validation_of_status_code(int(input("Enter your response code : ")))