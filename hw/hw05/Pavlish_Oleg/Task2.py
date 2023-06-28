n=int(input('Digit: '))
k,z=0,0
while k<n:
    print(k)
    if k==0:
        k+=1
    else:
        k+=z
        z=k-z


