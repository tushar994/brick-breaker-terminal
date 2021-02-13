from .baseState import *
from .dimensions.dimensions import *

class gameoverState(BaseState):
    def __init__(self):
        self.score = 0

    def enter(self, parameters):
        if('score' in parameters):
            self.score = parameters['score']
    
    def update(self,char):
        if(char=='s'):
            return ['pauseState' , {'gameover' : 1}]


    def render(self, display):
        for index,char in enumerate(game_over_string):
            for index2,char2 in enumerate(char):
                display[index][index2] = char2
        return display