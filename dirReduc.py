"""
a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". 
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, 
with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
How I crossed a mountain desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! 
So the task is to give to the man a simplified version of the plan. Annihilate opposite directions like N<->S and E<->W:
"""

# my solution
def dirReduc(arr):
    direction = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    a = []
    for i in arr:
        if a and direction[i] == a[-1]:
            print("before pop", a)
            a.pop()
        else:
            a.append(i)
            print("after append", a)
    return a


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# a = ["NORTH", "WEST", "SOUTH", "EAST"]
# a = ["NORTH", "NORTH", "WEST", "EAST"]
print(dirReduc(a))
