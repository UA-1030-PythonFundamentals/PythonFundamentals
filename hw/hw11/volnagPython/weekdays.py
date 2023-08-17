def num(den):
    ''' Sorting out  and handling data
    entered by user'''

    try:
        if den.isalpha():   # Checking if the characters in the string are alphabetic
            print(den + 5)
            
        if int(den) <= 0:   # Checking if the numeric characters in the string are positive
            #print(den)
            d = int("errror")
                  
    except TypeError:
        print("TypeError occured...")
        print(70*"*")
        return
    except ValueError:
        print("ValueError occured...")
        print(70*"*")
        return
    else:
        return int(den)
#VN
