def check_age(age):
    if age <= 0:
        raise ValueError("Incorrect age")


while True:
    try:
        age = int(input())
        check_age(age)
        print(age)
        break
    except ValueError:
        continue
