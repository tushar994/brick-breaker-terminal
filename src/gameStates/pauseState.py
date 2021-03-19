from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *
from .powerup import *
from .boss import *
from .bomb import *

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
        self.level = 1
        self.bullets = []
        self.bullet_shoot_time = 0
        self.boss = Boss(self.paddle.y + int(self.paddle.length/2))
        self.bombs = []

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
        lives_string = "level : " + str(self.level)
        for i,val in enumerate(lives_string):
            display[3][i] = val
        lives_string = "shooting time : " + str(self.paddle.shooting_time)
        for i,val in enumerate(lives_string):
            display[4][i] = val
        if(self.level==3):
            lives_string = "UFO health : " + "&"*self.boss.health
            for i,val in enumerate(lives_string):
                display[5][i] = val
        for ball in self.balls[:]:
            ball.render(display)

        display = self.paddle.render(display)
        for brick_row in self.bricks:
            for brick in brick_row:
                if(brick):
                    brick.render(display)
        for powerup in self.powerups:
            powerup.render(display)
        for bullet in self.bullets:
            bullet.render(display)
        # return display
        if(self.level==3):
            self.boss.render(display)
            for bomb in self.bombs:
                bomb.render(display)
        return display

    def update(self,input):
        if(self.gameover):
            self.paddle.update(input)
            # self.boss.update(input)
            self.balls[0].y = self.paddle.y
        if(input == 'p'):
            return ["playState", {"balls" : self.balls , "paddle" : self.paddle, "lives" : self.lives , "bricks" : self.bricks , "powerups" : self.powerups, "score":self.score , "time_played" : self.time_played, "level" : self.level, "bullets":self.bullets, "bullet_shoot_time":self.bullet_shoot_time, "boss":self.boss, "bombs" : self.bombs} ]

    def enter(self,parameters):
        if("balls" in parameters):
            self.balls = parameters['balls']
        if('paddle' in parameters):
            self.paddle.enter(parameters['paddle'])
        if('gameover' in parameters):
            self.gameover =  parameters['gameover']
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
        if('level' in parameters):
            self.level = parameters['level']
        if('bullets' in parameters):
            self.bullets = parameters['bullets']
        if('bullet_shoot_time' in parameters):
            self.bullet_shoot_time = parameters['bullet_shoot_time']
        if('boss' in parameters):
            self.boss = parameters['boss']
        if('bombs' in parameters):
            self.bombs = parameters['bombs']
        if len(self.bricks)==0:
            self.bricks = make_level(self.level)
