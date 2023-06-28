#HW5 PT7 - June 27, 2023
#Converting the set of integers into float type numbers
print(70*("*"))

    # Choosing the integer numbers
s = [2,4,6,4,9,0,1,13,25,3,23,67]
print("Our set of integers:", s)# List of integers
i = 0

    #Conversion of integers
for i in range(len(s)):
    s[i] = float(s[i])
    i += 1   

    #Printing results
print("We have a new set of float numbers:",s,end="\n")
print(70*("*"))

#VN
