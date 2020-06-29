"""
Q. find the maximum repeated character in the given sentence
"""
sentence = "This is a common interview question"
max_char = {i: sentence.count(i) for i in sentence}
print(sorted(max_char.items(), key=lambda kv: kv[1], reverse=True)[0])


# another soultion
# sentence = "This is a common interview question"
# max_char = {i: sentence.count(i) for i in sentence}
# for key, value in max_char.items():
#     if value == max(max_char.values()):
#         print(key)
