from .dimensions.dimensions import *

class Ball:
    def __init__(self):
        self.x = max_x -2
        self.y = 0
        self.dx = -1
        self.dy = 1
        self.time_y = 2
        self.time_x = 2
        self.current_x = 0
        self.current_y = 0
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

        if(parameters.time_y or parameters.time_y ==0):
            self.time_y = parameters.time_y

        if(parameters.time_x or parameters.time_x ==0):
            self.time_x = parameters.time_x

        if(parameters.current_x or parameters.current_x ==0):
            self.current_x = parameters.current_x
        if(parameters.current_y or parameters.current_y ==0):
            self.current_y = parameters.current_y


    def update(self, input):
        self.current_x+=1
        if(self.current_x>= self.time_x):
            self.x += self.dx
            self.current_x = 0
            if( self.x<=0):
                self.dx = -1*self.dx
                if(self.x<=0):
                    self.x = 0
                # if(self.x>=max_x-1):
                #     self.x = max_x-2
        self.current_y+=1
        if(self.current_y>= self.time_y):
            self.y += self.dy
            self.current_y = 0
            if(self.y>=max_y or self.y<=0):
                self.dy = -1*self.dy
                if(self.y<=0):
                    self.y = 0
                if(self.y>=max_y):
                    self.y = max_y-1

        # self.x>=max_x-1 or

    def render(self, display):
        display[self.x][self.y] = "0"
        return display