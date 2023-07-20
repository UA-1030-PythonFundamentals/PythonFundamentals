string = input("Enter a string:\n")
dict = {}

for char in string:
    keys = dict.keys()
    if char in keys:
        dict[char] = dict[char]+1
    else:
        dict[char] = 1

print(dict)