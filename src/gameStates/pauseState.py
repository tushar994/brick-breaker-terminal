from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *

class pauseState(BaseState):
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.ball.x = self.paddle.x -1 
        self.ball.y = self.paddle.y
        self.gameover = 1
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
                    brick.render(display)
        # return display
        return display

    def update(self,input):
        if(self.gameover):
            self.paddle.update(input)
            self.ball.y = self.paddle.y
        if(input == 'p'):
            return ["playState", {"ball" : self.ball , "paddle" : self.paddle, "lives" : self.lives , "bricks" : self.bricks} ]

    def enter(self,parameters):
        if("ball" in parameters):
            self.ball.enter(parameters['ball'])
        if('paddle' in parameters):
            self.paddle.enter(parameters['paddle'])
        if('gameover' in parameters):
            self.gameover =  0
        if('lives' in parameters):
            self.lives = parameters['lives']
        if('bricks' in parameters):
            self.bricks = parameters['bricks']
        if len(self.bricks)==0:
            self.bricks = make_level()
