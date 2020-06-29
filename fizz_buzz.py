# 3 % 3 == 0 which is less than 1 which return True and True = 1
def fizz_buzz(number):
    return "Fizz" * (number % 3 < 1) + "Buzz" * (number % 5 < 1) or number


print(fizz_buzz(5))


# for i in range(1, 16):
#     print("Fizz" * (i % 3 < 1) + "Buzz" * (i % 5 < 1) or i)

