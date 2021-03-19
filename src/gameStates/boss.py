from .dimensions.dimensions import *
from .bomb import *
from .brick import *
class Boss:
    def __init__(self,y):
        self.x = number_print_lines
        self.length = boss_length
        self.y = y-int(self.length/2)
        if(self.y<=0):
            self.y = 0
        if self.y+self.length -1 >=max_y:
            self.y = max_y - self.length
        self.speed = paddle_speed
        self.health = boss_health
        self.bomb_time = boss_drop_bomb_time
        self.bomb_time_left = 0
        self.defend = 2
        self.time_activate = 50
        self.time_left = 0
        self.activate_bricks = 0
    
    def update(self, input, bombs, bricks):
        # worrying about powerups
        # grab powerup
        # movement
        if input=='a':
            self.y-=self.speed
        if input=='d':
            self.y+=self.speed
        if self.y < 0:
            self.y = 0
        if self.y+self.length -1 >=max_y:
            self.y = max_y - self.length
        self.bomb_time_left += 1
        if(self.bomb_time_left >= self.bomb_time):
            self.bomb_time_left = 0
            bombs.append(Bomb(self.x, self.y + int(self.length/2)))
        if(self.health<=int(boss_health/2) and self.defend==2):
            self.activate_bricks = 1
        if(self.health<=int(boss_health/4) and self.defend==1):
            self.activate_bricks = 1
        if(self.activate_bricks):
            self.time_left += 1
            if(self.time_left>=self.time_activate):
                self.time_left = 0
                self.activate_bricks = 0
                self.defend_bricks(bricks)

    def render(self, display):
        for i in range(0,self.length):
            display[self.x][self.y + i] = "$"
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
        if(parameters.health or parameters.health==0):
            self.health = parameters.health
        if(parameters.boss_drop_bomb_time or parameters.boss_drop_bomb_time==0):
            self.boss_drop_bomb_time = parameters.boss_drop_bomb_time
        if(parameters.bomb_time or parameters.bomb_time==0):
            self.bomb_time = parameters.bomb_time
        if(parameters.defend or parameters.defend==0):
            self.defend = parameters.defend


    def defend_bricks(self, bricks):
        left_brick_x = (max_x - 3*brick_width)/2
        left_brick_y = (max_y - brick_y*brick_width)/3
        # print(bricks)
        # bricks[0] = []
        for j,brick in enumerate(bricks[0]):
            # print(j)
            bricks[0][j] =  Brick({'x': int(number_print_lines + 3) , 'y':int(j*brick_width) , 'level' : random.randint(1,4), 'explode' : 0, 'change' : 0,'no_power':1})
        self.defend -=1

    def collide_ball(self,ball):
        if(ball.x==number_print_lines+1 and ball.dx <=0):
            if(ball.y>=self.y - 1 and ball.y<=self.y+self.length):
                ball.dx = -1*ball.dx
                self.health -=1
                print("\a",end = "")
            