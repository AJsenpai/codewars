# find the sum of multiple of 3 and 5 below 10 or any given number
# mysolution


def solution(number):
    targetSum = 0
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            targetSum += i
        elif i % 5 == 0:
            targetSum += i
        elif i % 3 == 0:
            targetSum += i
        else:
            continue
    return targetSum


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution(10))
