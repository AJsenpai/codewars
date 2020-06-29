# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# For example:
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.
#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
#  persistence(4) = > 0  # Because 4 is already a one-digit numbe

# mysolution
def persistence(n):
    count = 0
    while len(str(n)) > 1:
        multiply = 1
        for num in str(n):
            multiply *= int(num)
        n = multiply
        count += 1
    return count


print(persistence(39))

# codewars
# solution 1
def persistence(n, count=0):
    return count if n < 10 else persistence(eval("*".join(list(str(n)))), count + 1)


# solution 2
import operator


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


# soultion 3
def multiply_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10

    return product


def persistence(n):
    count = 0
    while n > 9:
        n = multiply_digits(n)
        count += 1

    return count
