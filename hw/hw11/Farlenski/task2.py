while True:
    try:
        age = int(input())
        check_age(age)
        print(age)
    except:
        continue
    else:
        break