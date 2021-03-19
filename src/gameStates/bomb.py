from .dimensions.dimensions import *

class Bomb:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.dx = bomb_speed
        self.done = 0
        
    
    def enter(self, parameters):
        if('x' in parameters):
            self.x = parameters['x']
        if('y' in parameters):
            self.y = parameters['y']
        if('dx' in parameters):
            self.dx = parameters['dx']
        



    def update(self, input):
        self.x += self.dx
        if(self.x>=max_x-1):
            self.done = 1
            self.x = max_x-1

    def render(self, display):
        display[self.x][self.y] = "+"
        return display