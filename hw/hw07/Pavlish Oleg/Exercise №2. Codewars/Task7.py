def solution(number):
    solv=0
    if number<=0:
        return 0
    for k in range(0,number):
        if k%3==0 or k%5==0:
            solv+=k
    return solv