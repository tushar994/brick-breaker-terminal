from .dimensions.dimensions import *

class Ball:
    def __init__(self):
        self.x = max_x -2
        self.y = 0
        self.dx = -1
        self.dy = 1
        self.time_y = ball_standard_time
        self.time_x = ball_standard_time
        # these two map the time before the next move
        self.current_x = 0
        self.current_y = 0
        self.through = 0
        self.speed_left = 0
        self.through_left = 0
        # to see if it is stuck to paddle
        self.stuck = 0
        self.fireball = 0
        self.fireball_left = 0
    
    def enter(self, parameters):
        if('x' in parameters):
            self.x = parameters['x']
        if('y' in parameters):
            self.y = parameters['y']
        if('dx' in parameters):
            self.dx = parameters['dx']
        if('dy' in parameters):
            self.dy = parameters['dy']
        if('through' in parameters):
            self.through = parameters['through']
        if('through_left' in parameters):
            self.through_left = parameters['through_left']
        if('time_y' in parameters):
            self.time_y = parameters['time_y']
        if('time_x' in parameters):
            self.time_x = parameters['time_x']
        if('current_x' in parameters):
            self.current_x = parameters['current_x']
        if('current_y' in parameters):
            self.current_y = parameters['current_y']
        if('speed_left' in parameters):
            self.speed_left = parameters['speed_left']
        if('stuck' in parameters):
            self.stuck = parameters['stuck']
        if('fireball' in parameters):
            self.fireball = parameters['fireball']
        if('fireball_left' in parameters):
            self.fireball_left = parameters['fireball_left']



    def update(self, input):
        if(self.stuck):
            if input=='a':
                self.y-=paddle_speed
            if input=='d':
                self.y+=paddle_speed
            if input=='r':
                self.stuck = 0
        else:
            # updating position normally
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

        # worrying about powerups
        self.speed_left-=1
        if(self.speed_left<=0):
            if(abs(self.x)==2 and abs(self.y)==2):
                self.x = int(self.x/2)
                self.y = int(self.y/2)
            self.speed_left=0
        
        self.through_left-=1
        if(self.through_left<=0):
            self.through = 0
            self.through_left=0
        # self.x>=max_x-1 or
        self.fireball_left-=1
        if(self.fireball_left<=0):
            self.fireball = 0
            self.fireball_left = 0

    def render(self, display):
        display[self.x][self.y] = "0"
        return display
    
    def double_speed(self):
        if(abs(self.x)==1 and abs(self.y)==1):
            self.x *= 2
            self.y*=2
        self.speed_left = powerup_time
        
    def through_power(self):
        self.through = 1
        self.through_left = powerup_time
    
    def fireball_power(self):
        self.fireball = 1
        self.fireball_left = fireball_powerup_time