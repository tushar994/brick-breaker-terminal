from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *

class playState(BaseState):
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.lives = 3
        self.bricks = []

    def render(self,display):
        lives_string = "lives : " + str(self.lives)
        for i in range(0, 9):
            display[0][i] = lives_string[i]
        display = self.ball.render(display)
        display = self.paddle.render(display)
        for brick_row in self.bricks:
            for brick in brick_row:
                if(brick):
                    display = brick.render(display)
        return display

    def update(self,input):
        self.ball.update(input)
        self.paddle.update(input)
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    brick.update(self.bricks,index1, index2)
        if(input=='p'):
            return ["pauseState", {"ball" : self.ball , "paddle" : self.paddle , "gameover" : 0 , "lives" : self.lives, "bricks":self.bricks} ]
        #================================ this handles bal + paddle ================================================================================
        # check if it can hit  the paddle
        if(self.ball.x == max_x-2 and self.ball.dx >= 0):
            # check if contact with paddle has been madde
            if(self.ball.y >= self.paddle.y -1 and self.ball.y <= self.paddle.y + self.paddle.length ):
                self.ball.dx = -1 * self.ball.dx
                # now we change the dy according to where on the paddle it hit
                if(self.ball.y< int(self.paddle.y + self.paddle.length/2) and input=='a'):
                    self.ball.dy = -1 + -1*(int(self.paddle.y + self.paddle.length/2) - self.ball.y)
                elif(self.ball.y>int(self.paddle.y + self.paddle.length/2) and input=='d'):
                    self.ball.dy = 1 + -1*(int(self.paddle.y + self.paddle.length/2) - self.ball.y)
        #================================ finish bal + paddle ================================================================================


        #================================ this handles bal + brick ================================================================================
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    brick.ball_collide(self.ball, self.bricks,index1, index2)

        if(self.ball.x > max_x-2):
            return ["pauseState", {  "gameover" : 1 , "lives" : self.lives -1 , "bricks":self.bricks } ]

        return []
    def enter(self,parameters):
        if('ball' in parameters):
            self.ball.enter(parameters['ball'])
        if('paddle' in parameters):
            self.paddle.enter(parameters['paddle'])
        if('lives' in parameters):
            self.lives = parameters['lives']
        if('bricks' in parameters):
            self.bricks = parameters['bricks']
        if(len(self.bricks)==0):
            self.bricks = make_level()
