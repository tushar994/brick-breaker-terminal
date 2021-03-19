from .dimensions.dimensions import *

class Paddle:
    def __init__(self):
        self.x = max_x-1
        self.length = paddle_length
        self.y = max_y - self.length 
        self.speed = paddle_speed
        self.powerup_time = 0
        self.grab = 0
        self.grab_time = 0
        self.shooting = 0
        self.shooting_time = 0
    
    def update(self, input):
        # worrying about powerups
        # grab powerup
        self.grab_time-=1
        if(self.grab_time<=0):
            self.grab = 0
            self.grab_time=0
        # length powerup
        self.powerup_time -=1
        if self.powerup_time<=0:
            self.length = paddle_length
            self.powerup_time = 0
        self.shooting_time -=1
        if(self.shooting_time<=0):
            self.shooting = 0
            self.shooting_time =0
        # movement
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
        if(self.shooting):
            display[max_x-2][self.y + int(self.length/2)] = "!"
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
        if(parameters.powerup_time or parameters.powerup_time==0):
            self.powerup_time = parameters.powerup_time
        if(parameters.grab or parameters.grab==0):
            self.grab = parameters.grab
        if(parameters.grab_time or parameters.grab_time==0):
            self.grab_time = parameters.grab_time
        if(parameters.shooting or parameters.shooting==0):
            self.shooting = parameters.shooting
        if(parameters.shooting_time or parameters.shooting_time==0):
            self.shooting_time = parameters.shooting_time

    def make_longer(self):
        if(self.length == paddle_short_length):
            self.length = paddle_length
            self.powerup_time = 0
        else:
            self.length = paddle_long_length
            self.powerup_time = powerup_time
            if(self.y+ self.length -1 >= max_y):
                self.y = max_y - self.length
    
    def make_shorter(self):
        if(self.length == paddle_long_length):
            self.length = paddle_length
            self.powerup_time = 0
        else:
            self.length = paddle_short_length
            self.powerup_time = powerup_time

    def start_grab(self):
        self.grab = 1
        self.grab_time = powerup_time
    
    def start_shooting(self):
        self.shooting = 1
        self.shooting_time = shooting_time_period