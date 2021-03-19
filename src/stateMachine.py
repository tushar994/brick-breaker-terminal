
import numpy as np
from src.gameStates.dimensions.dimensions import *
from colorama import Fore, Style

class EmptyState:
    def render(self):
        return
    def update(self, char):
        return
    def enter(self):
        return
    def exit(self):
        return



printer_text = 1

class StateMachine:
    def __init__(self,state_list):
        self.empty = EmptyState()
        self.currentState = self.empty
        self.stateList = state_list
        self.printer_text = 1
    
    
    def changeState(self, newState, parameters = {}):
        if newState in self.stateList:
            self.currentState.exit()
            self.currentState = self.stateList[newState]()
            self.currentState.enter(parameters)
    
    def update(self, char):
        changeState = self.currentState.update(char)
        if changeState:
            if(changeState[0] and changeState[1]):
                self.changeState(changeState[0] , changeState[1])
            elif(changeState[0]):
                self.changeState(changeState[0])            
    
    def render(self):
        display = np.full((max_x,max_y), " ")
        display = self.currentState.render(display)
        
        for index, val in enumerate(display):
            # print(val)
            # print(self.printer_text, end = "")
            # print("::", end = "")
            # print(index, end = "")
            print("|", end = "")
            for valu in val:
                if(valu=="x"):
                    print(f"{Fore.RED}#{Style.RESET_ALL}",end = "")
                elif(valu=="k"):
                    print(f"{Fore.YELLOW}#{Style.RESET_ALL}",end = "")
                elif(valu=="q"):
                    print(f"{Fore.MAGENTA}#{Style.RESET_ALL}",end = "")
                elif(valu=="b"):
                    print(f"{Fore.BLUE}#{Style.RESET_ALL}",end = "")
                elif(valu=="z"):
                    print(f"{Fore.CYAN}#{Style.RESET_ALL}",end = "")
                elif(valu=="R"):
                    print(f"{Fore.RED}@{Style.RESET_ALL}",end = "")
                elif(valu=="Y"):
                    print(f"{Fore.YELLOW}@{Style.RESET_ALL}",end = "")
                elif(valu=="M"):
                    print(f"{Fore.MAGENTA}@{Style.RESET_ALL}",end = "")
                elif(valu=="B"):
                    print(f"{Fore.BLUE}@{Style.RESET_ALL}",end = "")
                elif(valu=="C"):
                    print(f"{Fore.CYAN}@{Style.RESET_ALL}",end = "")
                elif(valu=="S"):
                    print(f"{Fore.YELLOW}S{Style.RESET_ALL}",end = "")
                elif(valu=="F"):
                    print(f"{Fore.RED}F{Style.RESET_ALL}",end = "")
                else:
                    print(valu,end = "")
                    
            print("|")
        for val in display:
            print("\033[F", end = "")

