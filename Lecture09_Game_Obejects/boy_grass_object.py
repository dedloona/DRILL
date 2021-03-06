import math

from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = 0,90
        self.frame = 7

    def update(self): # 소년의 행위 구현
        self.x += 1
        self.frame = (self.frame + 1)%8


    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100 ,100 ,self.x, self.y)
    def rotate(self):
        pi = math.pi
        
        
        r = 1.5708
        self.image.clip_composite_draw(self.frame*100, 0, 100,100,r*4, 'None' , self.x, self.y,100,100)





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

grass = Grass()
boy = Boy()

# team = [ Boy() for i in range(11) ]

running = True

# game main loop code

while running:

    handle_events() # 키입력

    # Game logic
    boy.update()
    # Game drawing
    clear_canvas()
    grass.draw()
    boy.rotate()

    update_canvas()

    delay(0.03)


# finalization code
