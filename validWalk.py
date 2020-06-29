"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- 
everytime you press the button it sends you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to traverse one city 
block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's standing still!).
"""

# my solution 1
def is_valid_walk(walk):
    if (
        walk.count("e") == walk.count("w")
        and walk.count("s") == walk.count("n")
        and len(walk) == 10
    ):
        return True
    return False


# my solution 2
def is_valid_walk(walk):
    e, w, n, s = 0, 0, 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == "n":
                n += 1
            if i == "s":
                s += 1
            if i == "e":
                e += 1
            if i == "w":
                w += 1

        if s == n or e == w:
            return True
    return False


# some test cases for you...
# print(is_valid_walk(["e", "w", "e", "w", "n", "w", "n", "s", "e", "w"]))
# print(is_valid_walk(["e", "w", "n", "e", "n", "w", "e", "s", "w", "s"]))
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');
