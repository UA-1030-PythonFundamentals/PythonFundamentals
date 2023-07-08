def c(word):
    d={}
    for k in word:
        d[k]=word.count(k)
    return d
print(c('Letter'))