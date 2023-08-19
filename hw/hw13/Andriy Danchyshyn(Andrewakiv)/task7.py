def slices(func):
    def wrapper(*args, **kwargs):
        print('<\ ^^^^^^^ />')
        func(*args, **kwargs)
        print('<\ ______ />')
    return wrapper


@slices
def sandwich(*args):
    for i in args:
        print(i, end='\n')


sandwich('#tomato#', '-meat-', '~salad~')
