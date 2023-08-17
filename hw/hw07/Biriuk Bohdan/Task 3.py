def rec(word):
    d = {}
    for l in word:
        d[l] = word.count(l)
    return d
print(rec("qwerty"))