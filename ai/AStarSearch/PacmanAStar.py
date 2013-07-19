#!/usr/bin/python
# Head ends here

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

def manhattan(node, food):
    return abs(node[0] - food[0]) + abs(node[1] - food[1])

def print_result(parent_map, cost, goal):
    print(cost)
    path = []
    curr = goal
    while curr != None:
        path.append(curr)
        curr = parent_map.get(curr)
    path.reverse()
    # print(len(path)-1)
    for x in path:
        print(*x)

def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    start = (pacman_x, pacman_y)
    queue = [start]
    closed = []
    cost_map = {start:0}
    parent_map = dict()
    while queue:
        temp_cost_list = []
        for x in queue:
            temp_cost_list.append(cost_map[x] + manhattan(x, (food_x, food_y)))
            if cost_map[x] + manhattan(x, (food_x, food_y)) == min(temp_cost_list):
                node = x
        cost = cost_map[node]
        queue.remove(node)
        closed.append(node)
        if node == (food_x, food_y):
            print_result(parent_map, cost, node)
            break
        for n in get_adjacent(node[0], node[1], grid):
            if n not in closed:
                if n not in queue:
                    queue.append(n)
                    cost_map[n] = cost + 1
                    parent_map[n] = node
                elif cost + 1 < cost_map[n]:
                    cost_map[n] = cost + 1
                    parent_map[n] = node

if __name__ == '__main__':
    pacman_x, pacman_y = [ int(i) for i in input().strip().split() ]
    food_x, food_y = [ int(i) for i in input().strip().split() ]
    x, y = [ int(i) for i in input().strip().split() ]
    grid = []
    for i in range(0, x):
        grid.append(input().strip())
    
    nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid)
