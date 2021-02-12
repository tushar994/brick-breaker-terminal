from .dimensions.dimensions import *
import numpy as np
import colorama


# color for different levels of bricks
# 0-3 is for levels 1-4
# 4 is for indestructible
# 5 is for exploding
brick_colours = [
    "r",
    "b",
    "m",
    "c",
    "#",
    "y",
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
            text = "y"
        else:
            text = brick_colours[self.level - 1]
        
        display[self.x][self.y] = text
        display[self.x][self.y+1] = text
        display[self.x+1][self.y+1] = text
        display[self.x+1][self.y] = text
        return display

    def enter(self,parameters):
        if(parameters.x):
            self.x = parameters.x
        if(parameters.y):
            self.y = parameters.y
        if(parameters.length):
            self.length = parameters.length
    
    def update(self,bricks, index1,index2):
        if(self.done):
            bricks[index1][index2] = None
            # print("brick array is ", end="")
            # print(bricks[index1])
            # bricks[index1] = np.delete(bricks[index1],[index2])

    def ball_collide(self, ball, bricks, index1, index2):
        # if the ball collides with the brick
        if(not (ball.x > self.x + 2 or ball.x + 1< self.x or ball.y > self.y + 2 or ball.y + 1< self.y)):
            shift_x = 0
            shift_y = 0
            # check if it hit in y direction
            if((ball.y >= self.y -1 or ball.y <=self.y +2) and (ball.x >= self.x and ball.x <= self.x + 1)):
                ball.dy = -1*ball.dy
                if(ball.y >= self.y -1):
                    ball.y = self.y -2
                else:
                    ball.y = self.y +3
            # check if it hit in x direction
            elif((ball.x >= self.x -1 or ball.x <=self.x +2) and (ball.y >= self.y and ball.y <= self.y + 1)):
                ball.dx = -1*ball.dx
                if(ball.x >= self.x -1):
                    ball.x = self.x -2
                else:
                    ball.x = self.x +3
            else:
                if((ball.x <=  self.x and ball.dx > 0) or (ball.x >  self.x + 1 and ball.dx < 0)):
                    ball.dx *= -1
                else:
                    ball.dy *= -1
            if(self.level < 5):
                self.level -=1
            if self.level ==0:
                self.done = 1
                self.update(bricks,index1,index2)