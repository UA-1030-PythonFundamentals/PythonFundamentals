while True:
    user_login = input("Enter your login: ")
    if user_login.lower() == "first":
        print("Hello, " + user_login + "! Welcome!")
        break
    else:
        print("Error: Invalid login. Please try again.")