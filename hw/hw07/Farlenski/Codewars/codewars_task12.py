def correct_tail(body, tail):
    return True if body[-1] == tail else False


print(correct_tail("Fox", "x"))
print(correct_tail("Rhino", "o"))
print(correct_tail("Meerkat", "t"))
print(correct_tail("Emu", "t"))
print(correct_tail("Badger", "s"))
print(correct_tail("Giraffe", "d"))