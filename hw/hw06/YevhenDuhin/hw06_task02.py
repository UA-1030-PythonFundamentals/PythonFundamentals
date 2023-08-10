def login_check():
    login = input("Enter login: ")

    while login != "First":
        print("Error: Invalid login!")
        login = input("Enter login again: ")

    print("Welcome, user!")

login_check()
