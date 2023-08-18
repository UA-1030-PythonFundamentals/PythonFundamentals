##All these numbers in the list have a string data type, for example
##['1', '2', '3', '4', '5', '7'], convert this list to a list, all numbers of
##which have the data type integer :
##1) using the append method
##2) using the map method --HW13---Aug 14, 2023

print(70*"*")
a =['1', '2', '3', '4', '5', '7']

#############---Creating a map object of integers (map method)---######3

int_str = map(int, a)   #Generates a map object applying
                        #a function "int" to each element of a
print("Result :",list(int_str))    #Yields all items in int_str object

##try:
##    for i in range(len(a)):
##        print(next(int_str))
##        raise StopIteration
##except StopIteration:
##    print("StopIteration Error occured and handled")
##
##finally:
##    print(list(int_str))
    



#############---Creating a list of integers (append method)---######3
print(70*"*")
c=[]
for i in range(len(a)):
    a[i]=int(a[i])
    c.append(a[i])

print("Result :",c)
print(70*"*")
