#!/usr/bin/python

# Head ends here

def mark(x, y, grid):
    grid[x] = grid[x][0:y] + 'E' + grid[x][y + 1:]
    return grid

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

def nextMove(x, y, pacx, pacy, food_x, food_y, grid):
    queue = []
    ret = []
    parentMap = dict()
    queue.append((pacx, pacy))
    flag = True
    while queue and flag:
        tmp = queue.pop(0)
        # print('tmp',tmp)
        ret.append(tmp)
        adjs = get_adjacent(tmp[0], tmp[1], grid)
        # print('adjs',adjs)
        for adj in adjs:
            queue.append(adj)
            grid = mark(adj[0], adj[1], grid)
            parentMap[adj] = tmp
        if tmp == (food_x, food_y):
            flag = False
    path = []
    curr = (food_x, food_y)
    while (curr != None):
        path.append(curr)
        try:
            curr = parentMap[curr]
        except KeyError:
            curr = None
    path.reverse()
    print(len(ret))
    for x in ret:
        print(*x)
    print(len(path) - 1)
    for x in path:
        print(*x)
    
pacman_x, pacman_y = [ int(i) for i in input().strip().split() ]
food_x, food_y = [ int(i) for i in input().strip().split() ]
x, y = [ int(i) for i in input().strip().split() ]

grid = []
for i in range(0, x):
    grid.append(input().strip())

nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid)
