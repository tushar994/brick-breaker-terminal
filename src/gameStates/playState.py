from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *
from .powerup import *

class playState(BaseState):
    def __init__(self):
        self.balls = [Ball()]
        self.paddle = Paddle()
        self.lives = 3
        self.score = 0
        self.bricks = []
        self.powerups = []
        self.time_played = 0

    def render(self,display):
        lives_string = "lives : " + str(self.lives) 
        for i,val in enumerate(lives_string):
            display[0][i] = val
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
                    display = brick.render(display)
        for powerup in self.powerups:
            powerup.render(display)
        return display

    def update(self,input):
        self.time_played+=1
        for ball in self.balls[:]:
            ball.update(input)
        self.paddle.update(input)
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    brick.update(self.bricks,index1, index2,self.powerups , self)
        for index, powerup in enumerate(self.powerups):
            powerup.update(self.powerups, index)
        if(input=='p'):
            return ["pauseState", {"balls" : self.balls , "paddle" : self.paddle , "gameover" : 0 , "lives" : self.lives, "bricks":self.bricks , "powerups" : self.powerups, 'score':self.score , "time_played" : self.time_played} ]
        #================================ this handles ball + paddle ================================================================================
        for ball in self.balls[:]:
        # check if it can hit  the paddle
            if(ball.x == max_x-2 and ball.dx >= 0):
                # check if contact with paddle has been madde
                if(ball.y >= self.paddle.y -1 and ball.y <= self.paddle.y + self.paddle.length ):
                    if(self.paddle.grab):
                        ball.stuck=1
                    ball.dx = -1 * ball.dx
                    # now we change the dy according to where on the paddle it hit
                    if(ball.y< int(self.paddle.y + self.paddle.length/2) and input=='a'):
                        ball.time_y = int(top_paddle_hit/(int(self.paddle.y + self.paddle.length/2) - ball.y))
                        ball.dy = -1* abs(ball.dy)
                    elif(ball.y>int(self.paddle.y + self.paddle.length/2) and input=='d'):
                        ball.time_y = int(top_paddle_hit/(-1*(int(self.paddle.y + self.paddle.length/2) - ball.y)))
                        ball.dy = abs(ball.dy)
                    if(ball.time_y<=0):
                        ball.time_y = 1
        #================================ finish bal + paddle ================================================================================


        #================================ this handles bal + brick ================================================================================
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    for ball in self.balls:
                        brick.ball_collide(ball, self.bricks,index1, index2, self.powerups, self)
        #================================ finish bal + brick ================================================================================
        #================================ this handles powerup + paddle ================================================================================

        for index, powerup in enumerate(self.powerups):
            # if powerup collides with paddle
            if(powerup.x == max_x-1 and powerup.y >= self.paddle.y and powerup.y < self.paddle.y + self.paddle.length):
                # handle powering up
                if(powerup.type==0):
                    # paddle length increase powerup
                    self.paddle.make_longer()
                elif(powerup.type==1):
                    # paddle length decrease powerup
                    self.paddle.make_shorter()
                elif(powerup.type==1):
                    # paddle length decrease powerup
                    self.paddle.make_shorter()
                elif(powerup.type==2):
                    # add a new ball for all balls already existing
                    for ball in self.balls[:]:
                        newBall = Ball()
                        newBall.enter({'x' : ball.x , 'y' : ball.y, 'dx' : ball.dx, 'dy' : -1*ball.dy, 'time_x' : ball.time_x , 'time_y' : ball.time_y,'current_y':ball.current_y, 'current_x' : ball.current_x, 'through' : ball.through,'through_left' : ball.through_left,'speed_left' : ball.speed_left, 'stuck' : ball.stuck})
                        self.balls.append(newBall)
                elif(powerup.type==3):
                    # speed up balls
                    for ball in self.balls:
                        ball.double_speed()
                elif(powerup.type==4):
                    # through balls
                    for ball in self.balls:
                        ball.through_power()
                elif(powerup.type==4):
                    # through balls
                    for ball in self.balls:
                        ball.through_power()
                elif(powerup.type==5):
                    self.paddle.start_grab()
                # remove powerup
                self.powerups[index].exist = 0
        # actually remove the powerups
        self.powerups = [powerup for powerup in self.powerups if powerup.exist != 0]
        #================================ finish powerup + paddle ================================================================================
        # remove balls from ball array that are None after making balls that dead None
        for index,ball in enumerate(self.balls):
            if(ball.x > max_x-2):
                self.balls[index] = None
        self.balls = [ball for ball in self.balls if ball]
        # check if any bballs and end game if none
        if len(self.balls)==0:
            if(self.lives ==1):
                return ["gameoverState" , {"score" : self.score}]
            else:
                return ["pauseState", {  "gameover" : 1 , "lives" : self.lives -1, 'score':self.score , "bricks":self.bricks, "time_played" : self.time_played } ]

        # check bricks and send to next level if all done
        if( len([brick for brick_arr in self.bricks for brick in  brick_arr  if brick and brick.level<5] ) ==0):
            return ["pauseState" , {"score" : self.score + 500, "time_played" : self.time_played , "lives" : self.lives , "gameover" : 1}]
        return []
    def enter(self,parameters):
        if('balls' in parameters):
            self.balls = parameters['balls']
        if('paddle' in parameters):
            self.paddle.enter(parameters['paddle'])
        if('lives' in parameters):
            self.lives = parameters['lives']
        if('score' in parameters):
            self.score = parameters['score']
        if('bricks' in parameters):
            self.bricks = parameters['bricks']
        if('powerups' in parameters):
            self.powerups = parameters['powerups']
        if('time_played' in parameters):
            self.time_played = parameters['time_played']
        if(len(self.bricks)==0):
            self.bricks = make_level()
