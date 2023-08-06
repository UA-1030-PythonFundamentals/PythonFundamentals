def num_of_char_in_string(s):
    d = {}
    s1 = set(s)
    for ch in s1:
        d.update({ch: s.count(ch)})
    return(d)

print(num_of_char_in_string('hello'))