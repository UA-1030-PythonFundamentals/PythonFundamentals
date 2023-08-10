# No yelling!

def filter_words(st):
    return ' '.join(st.split()).capitalize()


print(filter_words('now     THIS is REALLY interesting'))
