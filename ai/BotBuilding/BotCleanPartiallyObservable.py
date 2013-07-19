#!/usr/bin/python
# Head ends here

import random

X_DIR = { 1:'DOWN', -1:'UP' }
Y_DIR = { 1:'RIGHT', -1:'LEFT' }
DIR = { 0:X_DIR[1], 1:X_DIR[-1], 2:Y_DIR[1], 3:Y_DIR[-1] }

dirty = []

def sub(t):
    #print('in sub,', t)
    return t[1]-t[0]

def find_path(posa, posb):
    #print('in find_path,',posa,posb)
    v = list(map(sub, zip(posa,posb)))
    if v[0] != 0:
        print(X_DIR[v[0]/abs(v[0])])
    elif v[1] != 0:
        print(Y_DIR[v[1]/abs(v[1])])
    else:
        dirty.pop(dirty.index(posa))
        print('CLEAN')

def search_dirty(posx,posy):
    if posx==0 or (posx,posy) in [(1,3),(2,3)]:
        print('DOWN')
    elif posx==4 or (posx,posy) in [(2,1),(3,1)]:
        print('UP')
    elif posy==0 or (posx,posy) in [(1,1),(1,2)]:
        print('RIGHT')
    elif posy==4 or (posx,posy) in [(2,3),(3,3)]:
        print('LEFT')
    else:
        print(random.choice(('UP','DOWN','LEFT','RIGHT')))
        
def calc_distance(posa,posb):
    #print('in calc_distance',posa,posb)
    v = list(map(sub, zip(posa,posb)))
    return abs(v[0])+abs(v[1])

# Head ends here
def next_move(posx, posy, board):
    
    # search in sight
    for x in range(5):
        for y in range(5):
            if board[x][y]=='d':
                dirty.append((x,y))
                
    # target found, go towards
    if dirty:
        distance=[]
        for p in dirty:
            distance.append(calc_distance((posx,posy),p))
        for d in dirty:
            if d[0] in (0,4) and d[1] in (0,4):
                find_path((posx,posy),d)
                return
        find_path((posx,posy),dirty[distance.index(min(distance))])
        
    # searching mod
    else:
        # if on border, go into inner ring
        search_dirty(posx,posy)
            

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

