# You receive an API response code from your test script
# Write an if-else block to check whether the response is
# successful with (status code 200) or not

response_code = int(input("Enter response code : ").strip())

if response_code == 200:
    print("API request Passed")
else:
    print("API Request Failed")
