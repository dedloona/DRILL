from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def ch_move(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)
while True:
    for i in range(100):
        angle =  i * 2 * math.pi / 100
        x = (math.cos(angle) * 350)+400
        y = (math.sin(angle) * 250)+300
        ch_move(x,y)
    i = 0


close_canvas()
