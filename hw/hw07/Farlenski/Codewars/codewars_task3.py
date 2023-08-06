def filter_words(st):
    result = st.capitalize()
    result = ' '.join(result.split())
    return result


print(filter_words("WOW this is REALLY          amazing"))