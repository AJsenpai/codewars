"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""

import re

# my solution
def kebabize(string):
    new_string = re.sub(r"\d", "", string)
    return "".join(
        f"-{c.lower()}" if c.isupper() and index != 0 else c.lower()
        for index, c in enumerate(new_string)
    )


# not one liner
# def kebabize(string):
#     new_string = re.sub(r"\d", "", string)
#     kebab = ""
#     for index, i in enumerate(new_string):
#         if i.isupper() and index == 0:
#             kebab += f"{i.lower()}"
#         elif i.isupper():
#             kebab += f"-{i.lower()}"
#         else:
#             kebab += f"{i}"
#     return "".join(kebab)


print(kebabize("3MyCamelHas3Humps"))
print(kebabize("SOS"))

# codewars solution 1
# def kebabize(s):
#     s = "".join([i for i in s if not i.isdigit()])
#     kebablist = filter(None, re.split("([A-Z][^A-Z]*)", s))
#     print(list(kebablist))
#     return "-".join(x.lower() for x in kebablist)

# codewars solution 2
# def kebabize(s):
#     return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

# print(kebabize("3MyCamelHas3Humps"))
