# find the occurence of odd integer in an array

# my solution

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
        # if seq.count(num) % 2:
            return num

# if seq.count(num) % 2:
# could have used this as True is represent by any positive number and False is represented by 0

seq = [1, 1, 2, 3, 3, 1, 1]
print(find_it(seq))

# code war

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]




# test cases
Test Cases:
@Test.describe("Basic tests")
def fixed_tests():
    Test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
    Test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
    Test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
    Test.assert_equals(find_it([10]), 10)
    Test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)


@Test.describe("Random tests")
def rand_tests():
    from random import randint, choice, shuffle
    
    for _ in range(40):
        seq = sum([[randint(1, 20)] * (2 * randint(1, 3)) for _ in range(randint(1, 10))], [])
        exp = choice(seq)
        seq.append(exp)
        shuffle(seq)
        Test.assert_equals(find_it(seq), exp)