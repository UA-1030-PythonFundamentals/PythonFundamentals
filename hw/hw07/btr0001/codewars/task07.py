def solution(number):
    if number <= 0:
        return 0
    else:
        sum = 0
        for i in range(0, number):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
    return sum