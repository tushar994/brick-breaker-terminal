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
]

class Powerup:
    def __init__(self , x, y):
        self.x = x
        # self.type = random.randint(0,5)
        self.type = 5
        self.y = y
        self.speed = power_speed
        self.time = time_power
        self.text = power_colours[self.type]
        self.exist = 1
    
    def update(self, powerups, index):
        self.x += self.speed
        if(self.x >= max_x-1):
            self.time -=1
            self.x = max_x-1
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