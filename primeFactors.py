"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


# My Solution
def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    factors.append(n)
    result = ""
    for index, val in enumerate(factors):
        if val not in factors[:index]:
            if factors.count(val) <= 1:
                result += f"({val})"
            else:
                result += f"({val}**{factors.count(val)})"
    return result


print(primeFactors(7775460))

# CodeWars Solution

# def primeFactors(n):
#     ret = ''
#     for i in xrange(2, n + 1):
#         num = 0
#         while(n % i == 0):
#             num += 1
#             n /= i
#         if num > 0:
#             ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
#         if n == 1:
#             return ret
