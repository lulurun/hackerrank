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



def print_result(tree,cost, goal):
    print(cost)
    path = []
    curr = goal
    while (curr != None):
        path.append(curr)
        try:
            curr = tree[curr]
        except KeyError:
            curr = None
    path.reverse()
    for x in path:
        print(*x)


def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    frontier = [(pacman_x, pacman_y)]
    visited = []
    parent_map = dict()
    cost_map = {(pacman_x, pacman_y):0}
    while frontier:
        node = frontier.pop()
        cost = cost_map[node]
        visited.append(node)
        if node == (food_x, food_y):
            print_result(parent_map, cost, node)
        for n in get_adjacent(node[0], node[1], grid):
            if n not in visited:
                if n not in frontier:
                    frontier.append(n)
                    parent_map[n] = node
                    cost_map[n] = cost + 1
                elif cost_map[n] > cost + 1:
                    parent_map[n] = node
                    cost_map[n] = cost + 1


if __name__ == '__main__':
    pacman_x, pacman_y = [ int(i) for i in input().strip().split() ]
    food_x, food_y = [ int(i) for i in input().strip().split() ]
    x, y = [ int(i) for i in input().strip().split() ]
    grid = []
    for i in range(0, x):
        grid.append(input().strip())
    
    nextMove(x,y,pacman_x,pacman_y,food_x,food_y,grid)