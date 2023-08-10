def checker(password):
    alpha_l='abcdefghijklmnopqrstuvwxyz'
    alpha_up=alpha_l[::].upper()
    nums='0123456789'
    symbs='#@$'
    check_1, check_2,check_3,check_4=False, False, False, False
    if 6>len(password)>16:
        return False
    for k in password:
        if k in alpha_l:
            check_1=True
        elif k in alpha_up:
            check_2=True
        elif k in nums:
            check_3=True
        elif k in symbs:
            check_4=True
    return check_1 and check_2 and check_3 and check_4
s=input('Input your password: ')
print(checker(s))