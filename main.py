
from imports import *

stateList = {
    "playState" : lambda : playState(),
    "pauseState" : lambda : pauseState()
}
state_machine = StateMachine(stateList)
state_machine.changeState('pauseState')

x = 0
y = 0

printer_text = 1
printer = "time"
while 1:
    input = input_to(Get())
    if input=='q':
        quit()
    state_machine.update(input)
    state_machine.render()





















# x
# |(0,0),  (0,1)
# |(1,0)
# |
# |
# |
# |
# |
# |
# |__________________________________ y
# 