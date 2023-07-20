def solution(number):
    return 0 if number < 0 else sum(set([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]))


print(solution(10))
