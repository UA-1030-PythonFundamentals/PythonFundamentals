auth=False
while auth is False:
    login=input('Enter you login: ')
    if login=='First':
        print('Welcome back!')
        auth=True
    else:
        print('ERROR! Your login isn\'t the same!')