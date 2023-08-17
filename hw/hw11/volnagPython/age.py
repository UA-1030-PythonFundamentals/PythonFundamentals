import math


def num(age):
    '''Processing the value entered by customer'''
   
    try:
        if age.isalpha():
            print(age+5)  #Throws the TypeError if entered \
                          #charater is a letter
        
        age = int(age)

        if age <= 0:
            age = math.log10(age) #Throws the ValueError if \
                                  #entered integer is negative
            
        
    except ValueError:
        print("...Please enter the correct age value...")
        print(70*"*")
        return
    except TypeError:
        print("...TypeError Occurred and Handled...")
        return

    else:
        print("------OK------")

        return age

print(70*"*")

#VN --HW11--PT22--Aug.1, 2023
