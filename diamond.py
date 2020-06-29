"""
Description:
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"
"""

# my solution
def diamond(n):
    if n < 1 or not n % 2:
        return None
    s = ""
    for i in range(n):
        # Build asterisks for the line
        ast = "*" * (i * 2 + 1) if i <= n // 2 else "*" * ((n - i) * 2 - 1)
        # Add a line
        s += " " * int((n - len(ast)) / 2) + ast + "\n"
    return s


# code wars
def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n // 2) - i)
            diamond += "*" * (n - abs((n - 1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None


print(diamond(5))


# normal diamond
# def diamond(lines):
#     if lines < 0 or not lines % 2:
#         return None
#     mid = lines // 2

#     for i in range(lines):
#         if i <= mid:
#             print((lines - i) * " " + (i * 2 + 1) * "*")
#         else:
#             print((i + 1) * " " + ((lines - i) * 2 - 1) * "*")
