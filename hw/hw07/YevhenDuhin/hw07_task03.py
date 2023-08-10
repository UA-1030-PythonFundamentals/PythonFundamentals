def count_char(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

string = input("Enter a string: ")
result = count_char(string)
print(result)
