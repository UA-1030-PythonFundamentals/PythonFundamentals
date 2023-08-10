def count(word):

    """calculates the number of characters included in a given string"""
    
    c = {}
   
    for i in word:
        c[i] = c.get(i, 0) + 1
    
    print(c)
    return c

count("hello")
