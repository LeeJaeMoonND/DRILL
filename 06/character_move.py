#유튜브 링크 : https://www.youtube.com/watch?v=znNJxs5rLOQ
from pico2d import *
import math

os.chdir('c:/2DGP/Lecture04_2D_Rendering')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
angle= -90

def move_character(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

while(True):
    # 사각형 운동
    while x<750:
        move_character(x,y)
        x+=2
        delay(0.01)
    while y < 510:
        move_character(x,y)
        y+=2
        delay(0.01)
    while x > 50:
        move_character(x,y)
        x-=2
        delay(0.01)
    while y > 90:
        move_character(x,y)
        y-=2
        delay(0.01)
    while x < 400:
        move_character(x,y)
        x+=2
        delay(0.01)

    #원운동
    while(angle<=270):
        move_character(x,y)
        angle += 2
        x= 400+(210 * math.cos(angle/360 * 2 * math.pi))
        y= 300+(210 * math.sin(angle/360 * 2 * math.pi))
        delay(0.01)

    angle -=360


close_canvas()
