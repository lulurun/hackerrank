#!/usr/bin/python

# Head ends here


def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    pass


if __name__=='__main__':
    pacman_x, pacman_y = [ int(i) for i in input().strip().split() ]
    food_x, food_y = [ int(i) for i in input().strip().split() ]
    x, y = [ int(i) for i in input().strip().split() ]
    grid = []
    for i in range(0, x):
        grid.append(input().strip())
    
    nextMove(x,y,pacman_x,pacman_y,food_x,food_y,grid)