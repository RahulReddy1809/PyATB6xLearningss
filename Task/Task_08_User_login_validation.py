# check if the user able to login based on correct username & Password
# username : admin
# Password : 1234

# o/p: Login Successful
# o/p: Invalid credentials

username = str(input("Enter username : ").strip())
password = int(input("Enter Password : ").strip())

if username == "admin" and password == 1234:
    print("login successful")
else:
    print("invalid credentials")

