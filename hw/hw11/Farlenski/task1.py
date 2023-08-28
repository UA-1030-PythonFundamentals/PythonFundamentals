def check(login):
    test = login.lower()
    separetor = ['-', '-id', 'id']
    role, id = None, None
    for separ in separetor:
        try:
            role, id = test.split(separ)
        except ValueError:
            continue
        if role and id:
            break

    if role == "admin" or role == "employee" and id.isdigit():
        return True
    else:
        raise ValueError(f"incorrect login '{login}'")