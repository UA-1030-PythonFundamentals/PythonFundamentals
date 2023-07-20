def check_password(pwd):
    res = True
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for ch in pwd:
        if 'a' <= ch <= 'z':
            count1 += 1
        if 'A' <= ch <= 'Z':
            count2 += 1
        if '0' <= ch <= '9':
            count3 += 1
        if ch in ['$', '#', '@']:
            count4 += 1
    if count1 == 0:
        print('At least 1 letter must be between [a-z].')
        res = False
    if count2 == 0:
        print('At least 1 letter must be between [A-Z].')
        res = False
    if count3 == 0:
        print('At least 1 number must be between [0-9].')
        res = False
    if count4 == 0:
        print('At least 1 character must be from [$#@].')
        res = False
    if len(pwd) < 6:
        print('Minimum length 6 characters.')
        res = False
    if len(pwd) > 16:
        print('Maximum length 16 characters.')
        res = False
    if res:
        print('Password checked')


check_password('aZ@1111')