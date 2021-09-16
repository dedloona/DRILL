from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
check = 0
def ch_move(x0, y=90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.001)

while True:
    if check == 0:        
        for x in range (0, 800):
                ch_move(x)
                x += 2
                if x == 799:
                    for y in range(90,600):
                        ch_move(x, y)
                        y += 2
                        if y == 600:
                            for x2 in range(0, 800):
                                ch_move(x, y)
                                x -= 1
                                if (x2 == 799):
                                      for y2 in range(90,600):
                                        ch_move(x, y)
                                        y -= 1
                                        check = 1
    else:
        for i in range(100):
            angle =  i * 2 * math.pi / 100
            x = (math.cos(angle) * 350)+400
            y = (math.sin(angle) * 250)+300
            ch_move(x,y)
        check = 0
   
                
                                   
                                
                        
    
    
    
close_canvas()
