n = int(input('Enter number:'))
prevprev = 0
prev = 1

for num in range(n + 1):
    if num==0:
        print(0)
    elif num==1:
        print(1)
    else:
        print(prevprev + prev)
        prev, prevprev = prevprev + prev, prev