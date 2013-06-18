#!/usr/bin/python
# Head ends here

X_DIR = { 1:'DOWN', -1:'UP' }

Y_DIR = { 1:'RIGHT', -1:'LEFT' }

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
        print('CLEAN')
    

def calc_distance(posa,posb):
    #print('in calc_distance',posa,posb)
    v = list(map(sub, zip(posa,posb)))
    return abs(v[0])+abs(v[1])

# Head ends here
def next_move(posx, posy, dimx, dimy, board):
    dirty=[]
    distance=[]
    for x in range(dimx):
        for y in range(dimy):
            if board[x][y]=='d':
                dirty.append([x,y])
    #print(dirty)
    for p in dirty:
        distance.append(calc_distance([posx,posy],p))
    find_path((posx,posy),dirty[distance.index(min(distance))])

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dimx,dimy=[int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dimy)]
    #print(pos,board)
    #find_path([1,3],[3,-1])
    next_move(pos[0], pos[1], dimx, dimy, board)
