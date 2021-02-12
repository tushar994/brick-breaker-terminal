from .dimensions.dimensions import *

class Paddle:
    def __init__(self):
        self.x = max_x-1
        self.length = 5
        self.y = max_y - self.length 
        self.speed =2
    
    def update(self, input):
        if input=='a':
            self.y-=self.speed
        if input=='d':
            self.y+=self.speed
        if self.y < 0:
            self.y = 0
        if self.y+self.length -1 >=max_y:
            self.y = max_y - self.length

    def render(self, display):
        for i in range(0,self.length):
            display[max_x-1][self.y + i] = "="
        return display
    def enter(self,parameters):
        if(parameters.x  or parameters.x ==0):
            self.x = parameters.x
        if(parameters.y or parameters.y ==0):
            self.y = parameters.y
        if(parameters.length):
            self.length = parameters.length
        if(parameters.speed or parameters.speed==0):
            self.speed = parameters.speed