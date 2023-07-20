def reverse(st):
    st = ' '.join(st.split()[::-1])
    return st


print(reverse("Hello World"))
print(reverse("Hi There."))


