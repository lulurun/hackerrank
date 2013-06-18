#!/usr/bin/python

# Head ends here
def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    path=dfs(pacman_x, pacman_y, grid)
    print(len(path))
    for v in path:
        try:
            print(v[0], v[1])
        except IndexError:
            print(v)
    print(len(path) - 1)
    for v in path:
        try:
            print(v[0], v[1])
        except IndexError:
            print(v)
    return

def get_adjacent(vertex_x, vertex_y, grid):
    vertexex = []
    if vertex_x > 0 and grid[vertex_x - 1][vertex_y] in '-.':
        vertexex.append((vertex_x - 1, vertex_y))
    if vertex_y > 0 and grid[vertex_x][vertex_y - 1] in '-.':
        vertexex.append((vertex_x, vertex_y - 1))
    if vertex_y + 1 < len(grid[0]) and grid[vertex_x][vertex_y + 1] in '-.':
        vertexex.append((vertex_x, vertex_y + 1))
    if vertex_x + 1 < len(grid) and grid[vertex_x + 1][vertex_y] in '-.':
        vertexex.append((vertex_x + 1, vertex_y))
    return vertexex

def dfs(pacx, pacy, grid):
    stack=[]
    ret=[]
    stack.append((pacx,pacy))
    flag=True
    while stack and flag:
        tmp = stack.pop()
        #print('tmp',tmp)
        ret.append(tmp)
        grid[tmp[0]] = grid[tmp[0]][0:tmp[1]] + 'x' + grid[tmp[0]][tmp[1]+1:]
        adjs=get_adjacent(tmp[0], tmp[1], grid)
        #print('adjs',adjs)
        for adj in adjs:
            if grid[adj[0]][adj[1]]=='.':
                ret.append(adj)
                flag = False
            stack.append(adj)
        #print('stack',stack)
        #print(*grid,sep='\n')
    print(*grid,sep='\n')
    return ret

# Tail starts here

pacman_x, pacman_y = [ int(i) for i in input().strip().split() ]
food_x, food_y = [ int(i) for i in input().strip().split() ]
x,y = [ int(i) for i in input().strip().split() ]

grid = []
for i in range(0, x):
    grid.append(input().strip())

nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid)
