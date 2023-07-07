n = int(input('n: '))
arr = [0, 1]
while sum([arr[-2], arr[-1]]) <= n:
    arr.append(sum([arr[-2], arr[-1]]))
print(', '.join([str(i) for i in arr]))
