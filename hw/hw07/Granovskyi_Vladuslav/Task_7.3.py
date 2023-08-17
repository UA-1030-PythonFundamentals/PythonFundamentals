words = input("Write your words:")

def w(word):
    l = {}

    for i in word:
        l[i] = word.count(i)
    return l

print(w(words))