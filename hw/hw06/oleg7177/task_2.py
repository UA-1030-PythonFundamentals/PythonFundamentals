login = "First"
logined = False
while not logined:
    if input("Enter login") == "First":
        logined = True
        print("Hello")
    else:
        print("Error")