def parsing(word):
    answer = {}
    for elem in word:
        if elem not in answer:
            answer[elem] = word.count(elem)
    return answer


word = input("Enter your word: ")
print(parsing(word))