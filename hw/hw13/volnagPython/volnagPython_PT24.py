##Display a list of list items that have the values "red", ["red",
##"green", "black", "red", "brown", "red", "blue", "red", "red",
##“yellow”] using the filter function. --HW13--Aug 14,2023
a = [-1,2,-3,4,-5,6,-7,8,-9,10]

b = filter(lambda n: n < 0, a)
print(list(b))


c = ["red","green", "black", "red", "brown", "red", "blue", "red", "red","yellow"]
b = filter(lambda n: n =='red', c)
print(list(b))
