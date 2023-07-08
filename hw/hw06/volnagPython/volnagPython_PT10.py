##Task2. Write a script that checks the login that the user enters.
##If the login is "First", then greet the users. If the login is
##different, send an error message.
##(need to use loop while) --  HW10 -- July 5, 2023
print(70*"*")

num = input("Please enter your name:\n")
log = input("Please enter your login:\n")

while log == "First":
  print("Hello", num.upper(),"!")
  break
else:
  print("Error!")
  
print(70*"*")
#VN
