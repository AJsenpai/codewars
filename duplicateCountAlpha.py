

# my solution 1
def duplicate_count(text):
    repeat = [i for i in text.lower() if text.lower().count(i) > 1]
    return len(set(repeat))
    

# my solution 2
# def duplicate_count(text):
#     total = 0
#     for i in set(text.lower()):
#         if text.lower().count(i) > 1:
#             total += 1

#     return total


print(duplicate_count("Ssbcde"))
# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)
