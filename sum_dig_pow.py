"""
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. 
What's the use of saying "Eureka"? Because this sum gives the same number.
In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.
See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) 
and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:
sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
"""
# My solution
def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    sum_pow = []
    for i in range(a, b + 2):
        number = 0
        for j in range(1, len(str(i)) + 1):
            number += int(str(i)[j - 1]) ** j  # loop is starting from j = 1
            if number == i:
                sum_pow.append(number)

    return sorted(sum_pow)


# Codewars solution
def filter_func(a):
    return sum(int(d) ** (i + 1) for i, d in enumerate(str(a))) == a


def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b + 1))


print(sum_dig_pow(1, 10))
# test.describe("Example Tests")
# test.assert_equals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
# test.assert_equals(sum_dig_pow(90, 100), [])
# test.assert_equals(sum_dig_pow(89, 135), [89, 135])
