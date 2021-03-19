from .dimensions.dimensions import *
from datetime import datetime
import random

# 0-Expand Paddle
# 1. Shrink Paddle
# 2. Ball Multiplier
# 3. Fast Ball
# 4. Thru-ball
# 5. Paddle Grab

power_colours = [
    "R",
    "B",
    "M",
    "C",
    "@",
    "Y",
    "S",
    "F",
]

class Powerup:
    def __init__(self , x, y, dx, dy, time_x,time_y,current_x,current_y):
        self.x = x
        # self.type = random.randint(0,7)
        self.type = 7
        self.y = y
        self.speed = power_speed
        self.dx = dx
        self.dy = dy
        self.time_y = time_y
        self.time_x = time_x
        # these two map the time before the next move
        self.current_x = current_x
        self.current_y = current_y
        self.time = time_power
        self.text = power_colours[self.type]
        self.exist = 1
    
    def update(self, powerups, index):
        self.current_x += 1
        self.current_y += 1
        if(self.current_x>= self.time_x):
            self.x += self.dx
            self.dx += acceleration_gravity
            self.current_x = 0
        if(self.current_y>= self.time_y):
            self.y += self.dy
            self.current_y = 0

        if(self.x >= max_x-1):
            self.time -=1
            self.x = max_x-1
            self.dy = 0
            self.dx = 0
        if(self.x <= 0):
            self.x = 0
            self.dx = -1*self.dx
        if(self.y <= 0):
            self.y = 0
        if(self.y >= max_y -1):
            self.y = max_y -1
            self.dy = -1*self.dy
        if(self.time==0):
            self.exist = 0
            # destroy this powerup

    def render(self, display):
        display[self.x][self.y] = self.text
        return display

    def enter(self,parameters):
        if(parameters.x  or parameters.x ==0):
            self.x = parameters.x
        if(parameters.y or parameters.y ==0):
            self.y = parameters.y
        if(parameters.time or parameters.time ==0):
            self.time = parameters.time
        if(parameters.type or parameters.type==0):
            self.type = parameters.type
            self.text = power_colours[self.type]