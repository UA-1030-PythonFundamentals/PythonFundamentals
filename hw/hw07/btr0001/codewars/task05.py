def reverse(st):
    # Your Code Here
    st2 = st.split()
    st2.reverse()
    st = ' '.join(st2)
    return st


print(reverse(" Hi There."))
