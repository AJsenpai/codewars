"""
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
"""

# my solution


def row_sum_odd_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        if i == n:
            for number in range(i * (i - 1) + 1, (i * i) + i):
                if number % 2 != 0:
                    total_sum += number
    return total_sum


# code wars
def row_sum_odd_numbers(n):
    return n ** 3


row_sum_odd_numbers(5)
# print(row_sum_odd_numbers(10))
# Test.assert_equals(row_sum_odd_numbers(19), 6859)
