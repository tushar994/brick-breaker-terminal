from .baseState import *
from .dimensions.dimensions import *
from .ball import *
from .paddle import *
from .levelMaker import *
from .powerup import *
from .bullet import Bullet
from .boss import *
from .bomb import *

class playState(BaseState):
    def __init__(self):
        self.balls = [Ball()]
        self.paddle = Paddle()
        self.lives = 3
        self.score = 0
        self.bricks = []
        self.powerups = []
        self.time_played = 0
        self.drop_bricks_time = brick_fall_time
        self.level = 1
        self.bullets = []
        self.bullet_shoot_time = 0
        self.boss = Boss(self.paddle.y+int(self.paddle.length/2))
        self.bombs = []

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
                    display = brick.render(display)
        for powerup in self.powerups:
            powerup.render(display)
        for bullet in self.bullets:
            bullet.render(display)
        if(self.level==3):
            self.boss.render(display)
            for bomb in self.bombs:
                bomb.render(display)
        return display

    def update(self,input):
        if (input=='l'):
            return self.change_level()
        self.time_played+=1
        for ball in self.balls[:]:
            ball.update(input)
        if(self.level==3):
            for bomb in self.bombs:
                bomb.update(input)
            for index,bomb in enumerate(self.bombs):
                if(bomb.done):
                    self.bombs.pop(index)
        self.paddle.update(input)
        if(self.level==3):
            self.boss.update(input,self.bombs,self.bricks)
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    brick.update(self.bricks,index1, index2,self.powerups , self, None)
        for index, powerup in enumerate(self.powerups):
            powerup.update(self.powerups, index)
        if(input=='p'):
            return ["pauseState", {"balls" : self.balls , "paddle" : self.paddle , "gameover" : 0 , "lives" : self.lives, "bricks":self.bricks , "powerups" : self.powerups, 'score':self.score , "time_played" : self.time_played, "level" : self.level, "bullets":self.bullets, "bullet_shoot_time":self.bullet_shoot_time, "boss":self.boss, "bombs":self.bombs} ]
        # =============================== This handles bullets ==============================================
        # add bullets if relevant
        self.bullet_shoot_time+=1
        
        if(self.paddle.shooting==1 and self.bullet_shoot_time>=bullet_delay):
            self.bullets.append(Bullet(max_x-2,int(self.paddle.y+self.paddle.length/2)))
            self.bullet_shoot_time = 0
        for index,bullet in enumerate(self.bullets[:]):
            bullet.update(input)
            if(bullet.done):
                self.bullets.pop(index)
        
        # collision between bullets and bricks
        for index1, brick_array in enumerate(self.bricks):
            for index2,brick in enumerate(brick_array):
                if brick:
                    for bullet in self.bullets:
                        if(bullet.x >= brick.x and bullet.x <= brick.x + brick_width and bullet.y>=brick.y and bullet.y<=brick.y+brick_width):
                            bullet.done = 1
                            brick.done = 1
        # =======================ball + boss====================
        if(self.level==3):
            for ball in self.balls:
                self.boss.collide_ball(ball)                    
        #================================ this handles ball + paddle ================================================================================
        for ball in self.balls[:]:
        # check if it can hit  the paddle
            if(ball.x == max_x-2 and ball.dx >= 0):
                # check if contact with paddle has been madde
                if(ball.y >= self.paddle.y -1 and ball.y <= self.paddle.y + self.paddle.length ):
                    if(self.time_played >= self.drop_bricks_time):
                        is_game_over = self.drop_bricks()
                    if(self.paddle.grab):
                        ball.stuck=1
                    ball.dx = -1 * ball.dx
                    print("\a",end = "")
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
        for index1, brick_array in enumerate(self.bricks[:]):
            for index2,brick in enumerate(brick_array[:]):
                if brick:
                    for ball in self.balls:
                        brick.ball_collide(ball, self.bricks,index1, index2, self.powerups, self)
        #================================ finish bal + brick ================================================================================
        #================================ handles bomb + brick ================================================================================
        for bomb in self.bombs:
            if(bomb.x == self.paddle.x - 1 and bomb.y >= self.paddle.y and bomb.y <= self.paddle.y + self.paddle.length):
                self.lives -=1
                bomb.done = 1
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
                elif(powerup.type==6):
                    self.paddle.start_shooting()
                # fireball
                elif(powerup.type==7):
                    for ball in self.balls:
                        ball.fireball_power()
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
        if len(self.balls)==0 or self.lives == 0:
            if(self.lives ==1 or self.lives ==0 ):
                return ["gameoverState" , {"score" : self.score}]
            else:
                return ["pauseState", {  "gameover" : 1 , "lives" : self.lives -1, 'score':self.score , "bricks":self.bricks, "time_played" : self.time_played , "level" : self.level, "boss":self.boss} ]
        if(self.boss.health<=0):
            return ["gameoverState" , {"score" : self.score + 100000}]
        # check bricks and send to next level if all done
        if( (self.level<3 and len([brick for brick_arr in self.bricks for brick in  brick_arr  if brick and brick.level<5] ) ==0) or (self.level==3 and self.boss.health==0)):
            return self.change_level()
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
        if(len(self.bricks)==0):
            self.bricks = make_level(self.level)

    def drop_bricks(self):
        if(self.time_played >= self.drop_bricks_time):
            for index1, brick_array in enumerate(self.bricks):
                for index2,brick in enumerate(brick_array):
                    if brick:
                        brick.x += 1
                        if(brick.x + brick_width >= max_x):
                            self.lives = 0
    def change_level(self):
        self.level +=1
        if(self.level <=3):
            return ["pauseState", {  "gameover" : 1 , "lives" : self.lives, 'score':self.score +500, "time_played" : self.time_played , "level" : self.level , "boss":self.boss} ]
        else:
            return ["gameoverState" , {"score" : self.score}]