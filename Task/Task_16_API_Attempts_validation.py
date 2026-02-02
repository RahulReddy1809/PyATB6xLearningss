# An API sometimes failes due to network delays

# Write a program to retry API call 3 times until the response code be 200
# If it still fails after 3 tries, then print a failure message
# use a while loop with a counter
# Expected output example
# Attempt 1 : response 500
# Attempt 2 : response 200
# ✅ Test passed

attempt = 1
max_attempts = 3
response = None

while attempt <= max_attempts:
    response = int(input("Enter the response : "))
    if response == 200:
        print("✅ Test Passed")
    else:
        attempt = attempt+1
if response != 200:
    print("❌ Test failed after 3 attempts")


