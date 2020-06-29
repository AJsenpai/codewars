"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, 
he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""


# my solution (Refactored)
def iq_test(numbers):
    checklist = [int(x) % 2 for x in numbers.split()]
    print(checklist)
    if checklist.count(0) > 1:
        return checklist.index(1) + 1
    else:
        return checklist.index(0) + 1


# my solution
def iq_test(numbers):
    if numbers == "":
        return None
    checklist = [int(x) for x in numbers.split()]
    eveness = [x for x in checklist if x % 2 == 0]
    oddness = [y for y in checklist if y % 2]
    if len(eveness) == 1:
        return checklist.index(eveness[0]) + 1
    else:
        return checklist.index(oddness[0]) + 1


# print(iq_test("2 4 7 8 10"))
# print(iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46"))
print(iq_test(" "))


# codewars solution
# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

# codewars solution
# def iq_test(n):
#     n = [int(i) % 2 for i in n.split()]
#     if n.count(0) > 1:
#         return n.index(1) + 1
#     else:
#         return n.index(0) + 1


# print(iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46"))
