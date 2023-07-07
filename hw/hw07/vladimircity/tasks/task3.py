# Write a function that calculates the number of characters included in
# given string

def calculate_symbols(string):
    return {letter: string.count(letter) for letter in string}


print(calculate_symbols('hello'))
