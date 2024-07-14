import random

def strt_gm():
 
    m =[]
    for i in range(4):
        m.append([0] * 4)

    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    addition_of_new(m)
    return m

def addition_of_new(m):
 
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while(m[r] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
 
    m[r] = 2
 
def get_current_state(m):
 
    for i in range(4):
        for j in range(4):
            if(m[i][j]== 2048):
                return 'WON'

    for i in range(4):
        for j in range(4):
            if(m[i][j]== 0):
                return 'GAME NOT OVER'
 
    for i in range(3):
        for j in range(3):
            if(m[i][j]== m[i + 1][j] or m[i][j]== m[i][j + 1]):
                return 'GAME NOT OVER'
 
    for j in range(3):
        if(m[3][j]== m[3][j + 1]):
            return 'GAME NOT OVER'
 
    for i in range(3):
        if(m[i][3]== m[i + 1][3]):
            return 'GAME NOT OVER'
 
    return 'LOST'

def comp(m):

    changed = False
  
    new_m = []
 
    for i in range(4):
        new_m.append([0] * 4)
         
    for i in range(4):
        pos = 0

        for j in range(4):
            if(m[i][j] != 0):
                 
                new_m[i][pos] = m[i][j]
                 
                if(j != pos):
                    changed = True
                pos += 1
 
    return new_m, changed
 
def merge(m):
     
    changed = False
     
    for i in range(4):
        for j in range(3):
 
            if(m[i][j] == m[i][j + 1] and m[i][j] != 0):
 
                m[i][j] = m[i][j] * 2
                m[i][j + 1] = 0

                changed = True
 
    return m, changed
 
def reverse(m):
    new_m =[]
    for i in range(4):
        new_m.append([])
        for j in range(4):
            new_m[i].append(m[i][3 - j])
    return new_m
 
def transpose(m):
    new_m = []
    for i in range(4):
        new_m.append([])
        for j in range(4):
            new_m[i].append(m[j][i])
    return new_m
 
def move_left(grid):

    new_grid, changed1 = compress(grid)

    new_grid, changed2 = merge(new_grid)
     
    changed = changed1 or changed2
 
    new_grid, temp = compress(new_grid)

    return new_grid, changed
 
def move_right(grid):
 
    new_grid = reverse(grid)

    new_grid, changed = move_left(new_grid)
 
    new_grid = reverse(new_grid)
    return new_grid, changed
 
def move_up(grid):
 
    new_grid = transpose(grid)

    new_grid, changed = move_left(new_grid)
 
    new_grid = transpose(new_grid)
    return new_grid, changed
 
def move_down(grid):
 
    new_grid = transpose(grid)
 
    new_grid, changed = move_right(new_grid)
 
    new_grid = transpose(new_grid)
    return new_grid, changed
