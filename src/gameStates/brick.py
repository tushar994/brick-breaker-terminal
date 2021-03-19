from .dimensions.dimensions import *
import numpy as np
import colorama
from .powerup import *
import random
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
        self.change = 0
        self.no_power = 0
        if ("x" in config):
            self.x = config['x']
        if( "y" in config):
            self.y = config['y']
        if ("level" in config):
            self.level = config['level']
        if("explode" in config):
            self.explode = config['explode']
        if("change" in config):
            self.change = config['change']
        if("no_power" in config):
            self.no_power = config['no_power']
        

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
    
    def update(self,bricks, index1,index2 , powerups ,playstate, ball):
        if(self.done):
            playstate.score += brick_score_add
            bricks[index1][index2] = None
            if (random.randint(0,3)==3 and self.no_power==0):
                if ball:
                    powerups.append(Powerup(self.x,self.y,ball[0],ball[1],ball[2],ball[3],ball[4],ball[5]))
                else:
                    powerups.append(Powerup(self.x,self.y,0,0,1,1,0,0))
            if(self.explode):
                for i in range(-1,2):
                    for j in range(-1,2):
                        if((index1 + i) < brick_x and (index1 + i) >= 0 and (index2+j)>= 0 and (index2+j)< brick_y):
                            if(bricks[index1 + i][index2 + j]):
                                bricks[index1 + i][index2+j].done = 1
        if(self.change):
            self.level = self.level%5 + 1
            # print("brick array is ", end="")
            # print(bricks[index1])
            # bricks[index1] = np.delete(bricks[index1],[index2])

    def ball_collide(self, ball, bricks, index1, index2 , powerups, playstate):
        # if the ball collides with the brick
        if(not (ball.x > self.x + brick_width or ball.x + 1< self.x or ball.y > self.y + brick_width or ball.y + 1< self.y)):
            shift_x = 0
            shift_y = 0
            actually = 0
            self.change = 0
            ball_copy =  [ball.dx,ball.dy,ball.time_x,ball.time_y,ball.current_x,ball.current_y]
            if(ball.through):
                self.level = 0
                self.done = 1
                self.update(bricks,index1,index2, powerups, playstate, None)
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
                # make brick explode if ball is fireball
                if(actually):
                    print("\a",end = "")
                if(ball.fireball and actually):
                    self.done = 1
                    self.explode = 1
                if(self.level < 5 and actually):
                    self.level -=1
                if (self.level ==0 and actually):
                    self.done = 1
                    self.update(bricks,index1,index2, powerups, playstate, ball_copy)