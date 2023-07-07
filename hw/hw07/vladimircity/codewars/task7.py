# Multiples of 3 or 5

def solution(number):
    numbers = []

    for i in range(number):
        if not i % 3 or not i % 5:
            numbers.append(i)

    return sum(numbers)


print(solution(200))
