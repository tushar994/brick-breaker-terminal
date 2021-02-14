from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *
from .powerup import *

class pauseState(BaseState):
    def __init__(self):
        self.balls = [Ball()]
        self.paddle = Paddle()
        self.balls[0].x = self.paddle.x -1 
        self.balls[0].y = self.paddle.y
        self.gameover = 1
        self.lives = 3
        self.bricks = []
        self.powerups = []
        self.score = 0
        self.time_played = 0

    def render(self,display):
        lives_string = "lives : " + str(self.lives)
        for i in range(0, 9):
            display[0][i] = lives_string[i]
        score_string = " score:" + str(self.score)
        for i,val in enumerate(score_string):
            display[1][i] = val
        lives_string = "time_played : " + str(self.time_played) 
        for i,val in enumerate(lives_string):
            display[2][i] = val
        for ball in self.balls[:]:
            ball.render(display)

        display = self.paddle.render(display)
        for brick_row in self.bricks:
            for brick in brick_row:
                if(brick):
                    brick.render(display)
        for powerup in self.powerups:
            powerup.render(display)
        # return display
        return display

    def update(self,input):
        if(self.gameover):
            self.paddle.update(input)
            self.balls[0].y = self.paddle.y
        if(input == 'p'):
            return ["playState", {"balls" : self.balls , "paddle" : self.paddle, "lives" : self.lives , "bricks" : self.bricks , "powerups" : self.powerups, "score":self.score , "time_played" : self.time_played} ]

    def enter(self,parameters):
        if("balls" in parameters):
            self.balls = parameters['balls']
        if('paddle' in parameters):
            self.paddle.enter(parameters['paddle'])
        if('gameover' in parameters):
            self.gameover =  1
        if('lives' in parameters):
            self.lives = parameters['lives']
        if('bricks' in parameters):
            self.bricks = parameters['bricks']
        if('powerups' in parameters):
            self.powerups = parameters['powerups']
        if('score' in parameters):
            self.score = parameters['score']
        if('time_played' in parameters):
            self.time_played = parameters['time_played']
        if len(self.bricks)==0:
            self.bricks = make_level()
