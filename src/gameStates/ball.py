from .dimensions.dimensions import *

class Ball:
    def __init__(self):
        self.x = max_x -2
        self.y = 0
        self.dx = -1
        self.dy = 1
        self.through = 0
    
    def enter(self, parameters):
        if(parameters.x or parameters.x ==0):
            self.x = parameters.x
        if(parameters.y or parameters.y ==0):
            self.y = parameters.y
            # print("y is ", end = "")
            # print(parameters.y)
        if(parameters.dx or parameters.dx ==0):
            self.dx = parameters.dx
        if(parameters.dy or parameters.dy ==0):
            self.dy = parameters.dy
        if(parameters.through or parameters.through ==0):
            self.through = parameters.through


    def update(self, input):
        self.y += self.dy
        self.x += self.dx
        if(self.y>=max_y or self.y<=0):
            self.dy = -1*self.dy
            if(self.y<=0):
                self.y = 0
            if(self.y>=max_y):
                self.y = max_y-1
        # self.x>=max_x-1 or
        if( self.x<=0):
            self.dx = -1*self.dx
            if(self.x<=0):
                self.x = 0
            # if(self.x>=max_x-1):
            #     self.x = max_x-2

    def render(self, display):
        display[self.x][self.y] = "0"
        return display