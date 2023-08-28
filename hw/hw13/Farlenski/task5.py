def celsius_to_fahrenheit(temps):
    m = map(lambda x: x * 9 /5 +32 , temps)
    return list(m)