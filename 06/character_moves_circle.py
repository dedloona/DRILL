from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def ch_move(x0, y=90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.001)

grass.draw_now(400, 30)
character.draw_now(x, y)                       
                                

delay(3)          
    
    
    
close_canvas()
