def solution(number):
    if number > 0:
        counter = 0
        for i in range(number):
            if not i % 3 or not i % 5:
                counter += i
        return counter
    else:
        return 0


print(solution(6))