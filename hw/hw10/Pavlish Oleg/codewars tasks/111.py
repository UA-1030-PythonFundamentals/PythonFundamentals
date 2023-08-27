num=input('Numbers: ')
num_1, num_2 =num.split(',')
try:
    print(int(num_1)/int(num_2))
except ZeroDivisionError:
    print('Zero!')
except SyntaxError:
    print('Syntax')
except Exception:
    print('Exceptions')
else:
    print('Perfect')
finally:
    print('END')