login = input("Enter Login:\n")
true_login = "First"
count = 1
while login != true_login:
   
    print("Error, login is false.")
    count += 1
    login = input("Enter Login again:\n")

    if count == 2 and login != true_login:
        print("You forgot your login? Or you are bandit?!")
    if count == 3 and login != true_login:
        print("Last chance! I warning you.")
    if count == 4 and login != true_login:
        print("I'll call to police! Run away!!")
        break
    
if login == true_login:
    print(f"Great! You are entered.\nHello, {true_login} ;)")