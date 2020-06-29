"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


# my solution
def max_sequence(arr):
    current_max, total_max = 0, 0
    for value in arr:
        current_max += value
        if current_max < 0:
            current_max = 0
        if current_max > total_max:
            total_max = current_max
        print(current_max, total_max)
    return total_max


# code wars splution
# def maxSequence(arr):
#     max_low = 0
#     max_great = 0
#     for n in arr:
#         max_low = max(0, max_low + n)
#         max_great = max(max_great, max_low)
#         print(max_low, max_great)
#     return max_great


print(max_sequence([-2, -3, 4, 1, -5, -34]))
# print(maxSequence([-2, -3, 4, 1, -5, -34]))
