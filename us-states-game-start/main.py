from turtle import Screen, screensize
import turtle
from table import table
from statename import Statename

screen = Screen()
screen.title('U.S State Game')
img = 'blank_states_img.gif'
screen.bgpic(img)
statename= Statename()


game_is_on = True
correct = 0
while game_is_on:
    answer = screen.textinput(title=f'{correct}/50 State Correct', prompt="What's another state")
    answer =answer.title()
    if answer in table['state'].values:
        statename.create_name(answer,table['x'][table['state']==answer],table['y'][table['state']==answer])
        correct += 1
        
    if answer.title() == 'Exit':
        state_missing_frame = statename.missing_state()
        state_missing_frame.to_csv('missing.csv')
        break




# def get_mouse_click_coor(x,y): # get x,y coor of click by click on picture
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)





# turtle.mainloop() # == screen.exitonclick but not exit onclick
screen.exitonclick()