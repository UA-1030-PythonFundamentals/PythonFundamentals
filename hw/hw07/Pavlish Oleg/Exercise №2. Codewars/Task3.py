def filter_words(st):
    return ' '.join(st.capitalize().split())
print(filter_words('HELLO world!'))