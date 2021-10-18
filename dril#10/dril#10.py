from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class bigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(0,800)
        self.y = 599
    def draw(self):
        self.image.draw(self.x,self.y)
    def fall(self):
        self.y-=random.randint(1,10)
        if self.y<80:
            self.y = 80

class smallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(0,800)
        self.y = 599
    def draw(self):
        self.image.draw(self.x,self.y)
    def fall(self):
        self.y-=random.randint(1,10)
        if self.y<70:
            self.y = 70

class Boy:
    def __init__(self):
        self.x,self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame+1)%8
        self.x += random.randint(1,10)
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

n=random.randint(0,20)
open_canvas()
team = [Boy() for i in range(11)]
bigBallTeam=[bigBall() for i in range(n)]
grass = Grass()
smallBallTeam=[smallBall() for i in range(20-n)]
running = True
# initialization code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for bigBall in bigBallTeam:
        bigBall.fall()
    for smallBall in smallBallTeam:
        smallBall.fall()
    clear_canvas()


    for boy in team:
        boy.draw()
    for bigBall in bigBallTeam:
        bigBall.draw()
    for smallBall in smallBallTeam:
        smallBall.draw()
    grass.draw()
    update_canvas()

    delay(0.05)
# game main loop code

# finalization code