from .dimensions.dimensions import *
import numpy as np
import colorama
from .powerup import *

# color for different levels of bricks
# 0-3 is for levels 1-4
# 4 is for indestructible
# 5 is for exploding
brick_colours = [
    "x",
    "b",
    "q",
    "z",
    "#",
    "k",
]


class Brick:
    def __init__(self , config):
        self.x = 0
        self.y = 0
        self.level = 5
        self.explode = 0
        self.done = 0
        if ("x" in config):
            self.x = config['x']
        if( "y" in config):
            self.y = config['y']
        if ("level" in config):
            self.level = config['level']
        if("explode" in config):
            self.explode = config['explode']
    
    def update(self, input):
        if input=='a':
            self.y-=1
        if input=='d':
            self.y+=1
        if self.y < 0:
            self.y = 0
        if self.y+self.length -1 >=max_y:
            self.y = max_y - self.length

    def render(self, display):

        text = ""
        if(self.explode):
            text = brick_colours[5]
        else:
            text = brick_colours[self.level - 1]
        for i in range(0,brick_width):
            for j in range(0,brick_width):
                display[self.x+i][self.y+j] = text
        return display

    def enter(self,parameters):
        if(parameters.x):
            self.x = parameters.x
        if(parameters.y):
            self.y = parameters.y
        if(parameters.length):
            self.length = parameters.length
    
    def update(self,bricks, index1,index2 , powerups ,playstate):
        if(self.done):
            playstate.score += brick_score_add
            bricks[index1][index2] = None
            powerups.append(Powerup(self.x,self.y))
            if(self.explode):
                for i in range(-1,2):
                    for j in range(-1,2):
                        if((index1 + i) < brick_x and (index1 + i) >= 0 and (index2+j)>= 0 and (index2+j)< brick_y):
                            if(bricks[index1 + i][index2 + j]):
                                bricks[index1 + i][index2+j].done = 1
            # print("brick array is ", end="")
            # print(bricks[index1])
            # bricks[index1] = np.delete(bricks[index1],[index2])

    def ball_collide(self, ball, bricks, index1, index2 , powerups, playstate):
        # if the ball collides with the brick
        if(not (ball.x > self.x + brick_width or ball.x + 1< self.x or ball.y > self.y + brick_width or ball.y + 1< self.y)):
            shift_x = 0
            shift_y = 0
            actually = 0
            if(ball.through):
                self.level = 0
                self.done = 1
                self.update(bricks,index1,index2, powerups, playstate)
            else:
                # check if it hit in y direction
                if((ball.y <= self.y -1 or ball.y >=self.y +brick_width) and (ball.x >= self.x and ball.x <= self.x + brick_width -1)):
                    ball.dy = -1*ball.dy
                    if(ball.y <= self.y -1):
                        ball.y = self.y -2
                    else:
                        ball.y = self.y + brick_width + 1
                    actually =1
                # check if it hit in x direction
                elif((ball.x <= self.x -1 or ball.x >=self.x +brick_width) and (ball.y >= self.y and ball.y <= self.y + brick_width-1)):
                    ball.dx = -1*ball.dx
                    if(ball.x <= self.x -1):
                        ball.x = self.x -2
                    else:
                        ball.x = self.x + brick_width + 1
                    actually =1
                else:
                    if((ball.x == self.x-1) and (ball.y==self.y+brick_width) and (ball.dx>0) and (ball.dy<0)):
                        ball.dx *=-1
                        ball.dy *=-1
                        actually =1
                    elif((ball.x == self.x-1) and (ball.y==self.y-1) and (ball.dx>0) and (ball.dy>0)):
                        ball.dx *=-1
                        ball.dy *=-1
                        
                        actually =1
                    elif((ball.x == self.x+brick_width) and (ball.y==self.y+brick_width) and (ball.dx<0) and (ball.dy<0)):
                        ball.dx *=-1
                        ball.dy *=-1
                        actually =1
                    elif((ball.x == self.x+brick_width) and (ball.y==self.y-1) and (ball.dx<0) and (ball.dy>0)):
                        ball.dx *=-1
                        ball.dy *=-1
                        actually =1
                if(self.level < 5 and actually):
                    self.level -=1
                if (self.level ==0 and actually):
                    self.done = 1
                    self.update(bricks,index1,index2, powerups, playstate)