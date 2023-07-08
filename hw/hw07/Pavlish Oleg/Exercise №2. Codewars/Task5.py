def reverse(st):
    list=st.split()
    list=list[::-1]
    return ' '.join(list)
print(reverse('Hello World'))
print(reverse('Hi There.'))