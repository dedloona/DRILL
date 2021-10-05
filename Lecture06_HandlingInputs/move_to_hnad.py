from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        # x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def random_hand():
    global ax, ay
    ax = random.randint(0, 1280)
    ay = random.randint(0, 1024)
    arrow.draw(ax, ay)


def to_char():
    global x, y, ax, ay
    if ax < x:
        x = x - 1
        if ay < y:
            y = y - 1
        elif ay > y:
            y = y + 1
    elif ax > x:
        x = x + 1
        if ay < y:
            y = y - 1
        elif ay > y:
            y = y + 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
ax = 0
ay = 0

random_hand()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    random_hand()
    to_char()
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()




