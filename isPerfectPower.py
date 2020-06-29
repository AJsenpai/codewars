 import math

# my solution
def isPP(n):
    for i in range(2, math.isqrt(n) + 1):
        power = round(math.log(n, i))
        if i ** power == n:
            return [i, power]
    return None


print(isPP(5))

# codewar solution
def isPP(n):
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i ** j > n:
                break
            elif i ** j == n:
                return [i, j]
    return None



# won't work for six figures
# def isPP(n):
#     end = math.isqrt(n) + 1
#     result = [[x, y] for x in range(2, end) for y in range(2, end) if x ** y == n]
#     if result:
#         return result[-1]
#     return
