# Reversing Words in a String

def reverse(st):
    st = ' '.join(st.split()[::-1])

    return st


print(reverse('Reversing Words in a String'))
