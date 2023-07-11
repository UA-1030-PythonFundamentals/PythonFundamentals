while True:
    login = input("Enter your login:")
    if login == "First":
        print(f"Welcome, {login}!!!")
        break
    elif login == "q":
        print("Bye")
        break
    else:
        print(f"Your login doesn't exist. Please, try again!!!")