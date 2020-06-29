"""
Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 4 elements and each following 
element is the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian, but it would also 
sound really awful) with a signature of 5 elements and each following element is the sum of the 5 previous, and so on.

Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - and remember each next element is the 
sum of the last X elements - and returns the first n elements of the so seeded sequence.

xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}
xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}
xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}
xbonacci {1,1} produces the Fibonacci sequence

"""

# my solution
def Xbonacci(signature, n):
    xlist = signature[:n]
    for i in range(n - len(signature)):
        xlist.append(sum(xlist[i : i + len(xlist)]))
    return xlist


# print(xbonacci([0, 1], 10))
# print(xbonacci([1, 0, 0, 0, 0, 0, 1], 10))
# print(xbonacci([2, 1, 15, 14, 12, 2, 1, 10, 0, 13, 6, 7, 14, 11, 20, 5, 0], 12))
# Test.describe("Basic tests")
# Test.assert_equals(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
# Test.assert_equals(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
# Test.assert_equals(Xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])

# codewars solution
# def Xbonacci(signature,n):
#     output, x = signature[:n], len(signature)
#     while len(output) < n:
#         output.append(sum(output[-x:]))
#     return output
