from .dimensions.dimensions import *
from .brick import *
# Importing datetime.
from datetime import datetime
import random
import numpy as np

# Creating a datetime object so we can test.
a = datetime.now()

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
print(a)
random.seed(a)


def iterate(bricks, starting_x, starting_y, changes, first, one,left_brick_x,left_brick_y):
    add_x = starting_x
    add_y = starting_y
    add_x += one*changes[first]['x']
    add_y += one*changes[first]['y']
    total = 0
    while(add_x>=0 and add_x<brick_x and add_y>=0 and add_y<brick_y):
        bricks[add_x][add_y] = Brick({'x': int(add_x*2 + left_brick_x) , 'y': int(add_y*2 + left_brick_y) , 'level' : 1, 'explode' : 1})
        total+=1
        add_x += one*changes[first]['x']
        add_y += one*changes[first]['y']
    return [bricks,total]


def make_level():
    bricks = np.full((brick_x,brick_y), None)
    left_brick_x = (max_x - brick_x*2)/2
    left_brick_y = (max_y - brick_y*2)/3
    is_explode = random.randint(0,5)
    if(is_explode==5):
        is_explode = 1
    else:
        is_explode = 0

    # this sectin adds exploding bricks to the mix (ggggg)
    if is_explode:
        # find which brick is the first  exploding brick
        starting_x = random.randint(0,brick_x-1)
        starting_y = random.randint(0,brick_y-1)
        #  the array that dictates if the others are  diagonally or hhorizontally or whatever
        changes = [ {"x":1, "y":1}, {"x":1, "y":-1}, {"x":1, "y":0} ,{"x":0, "y":1} ]
        total = 0
        first = random.randint(0,3)
        bricks[starting_x][starting_y] = Brick({'x': int(starting_x*2 + left_brick_x) , 'y':int(starting_y*2 + left_brick_y) , 'level' : 1, 'explode' : 1})
        total += 1
        # first iteration in first direction
        final = iterate(bricks, starting_x, starting_y, changes, first,1,left_brick_x,left_brick_y)
        bricks= final[0]
        total += final[1]
        # second iteration in first direction's opposite
        final = iterate(bricks, starting_x, starting_y, changes,first, -1,left_brick_x,left_brick_y)
        bricks= final[0]
        total += final[1]

        if(total<6):
            second = random.randint(0,3)
            if(second==first):
                second += 1
                second = second % 4
            # first iteration in first direction
            final = iterate(bricks, starting_x, starting_y, changes,second, 1,left_brick_x,left_brick_y)
            bricks= final[0]
            total += final[1]
            # second iteration in first direction's opposite
            final = iterate(bricks, starting_x, starting_y, changes,second, -1,left_brick_x,left_brick_y)
            bricks= final[0]
            total += final[1]
        
    # now we add normal bricks if needed
    for i in range(0,brick_x):
        for j in range(0,brick_y):
            if(not( bricks[i][j])):
                yes = random.randint(0,4)
                if(yes==4):
                    bricks[i][j] = Brick({'x': int(i*2 + left_brick_x) , 'y':int(j*2 + left_brick_y) , 'level' : random.randint(1,5), 'explode' : 0})
    return bricks