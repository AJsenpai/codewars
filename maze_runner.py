"""
Task
You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. 
If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, 
you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.
 
The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
..with the following key

0 = Safe place to walk
1 = Wall
2 = Start Point
3 = Finish Point
 
direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"

Rules
1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
2. The start and finish positions will change for the final tests.
3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.
"""
# my solution
from pprint import pprint


def maze_runner(maze, directions):
    # maze.reverse()
    # pprint(maze)
    x, y = 0, 0
    for index, sublist in enumerate(maze):
        print(index, sublist)
        if 2 in sublist:
            x = index
            y = sublist.index(2)
            break
    for i in directions:
        if i == "N": x -= 1
        if i == "S": x += 1
        if i == "E": y += 1
        if i == "W": y -= 1

        if x < 0 or y < 0 or x > len(maze) - 1 or y > len(maze) - 1 or maze[x][y] == 1:
            return "Dead"
        if maze[x][y] == 3:
            return "Finish"
    
    return "Lost"


maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 3],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 0, 1],
]

print(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"]))
# test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
# test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
# test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")
