from turtle import Turtle
from table import table
import pandas as pd

table = table
ALIGNMENT = 'center'
FONT = ('Arial',14,'normal')
class Statename():
    def __init__(self):
        self.guess_state = []
        self.miss_state = []
    

    def create_name(self,state_name,x,y):
        name = Turtle()
        name.color('black')
        name.penup()
        name.hideturtle()
        name.goto(float(x),float(y))
        name.write(arg=state_name,align=ALIGNMENT,font=FONT)    
        self.guess_state.append(state_name)
    
    def missing_state(self):
        global table
        for state in table['state'].values:
            if state not in self.guess_state:
                self.miss_state.append(state)
            miss_state_frame = pd.DataFrame(self.miss_state)
        return miss_state_frame