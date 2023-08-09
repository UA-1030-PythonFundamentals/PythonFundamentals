def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def main():
    input_string = input("Enter a string: ")
    result = count_characters(input_string)
    print(result)

if __name__ == "__main__":
    main()
