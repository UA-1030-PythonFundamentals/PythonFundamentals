Name = input("Your name: ")
a = "First"
b = input("Login: ")
while b != a:
        print("Error, it's not correct login")
        b = input("Login: ")
        if b != a:
            print("Error, it's not correct login")
            b = input("Login: ")
            break
if b == a:
   print(f"Hello {Name}")

