from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

class Man():
    def __init__(self):
        self.image = load_image('man.png')
        self.frame = 0
        self.direction=0
        self.p = (self.x, self.y) = (400, 400)

    def move(self, n):
        self.frame = (self.frame + 1) % 8
        if n == 6:
            self.x += 5
            self.direction = 0
        elif n == 4:
            self.x -= 5
            self.direction = 2
        elif n == 5:
            self.y -= 5
            self.direction = 3
        elif n == 8:
            self.y += 5
            self.direction = 1

    def draw(self):
        self.image.clip_draw(self.frame*120, self.direction*130, 120, 130, self.x, self.y)

class Mon1():
    def __init__(self):
        self.image = load_image('mon1.png')
        self.frame = 0
        self.direction = 8
        self.p = (self.x, self.y) = (random.randint(100, 300), random.randint(100, 300))

    def draw(self):
        self.image.clip_draw(self.frame*134, self.direction*135, 134, 135, self.x, self.y)
    def move(self):
        self.x += random.randint(-5,5)
        self.y += random.randint(-5,5)
        self.frame = (self.frame+1)%5
def handle_events():
    global running
    global man
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                man.move(6)
            elif event.key == SDLK_LEFT:
                man.move(4)
            elif event.key == SDLK_DOWN:
                man.move(5)
            elif event.key == SDLK_UP:
                man.move(8)




open_canvas()
man = Man()
mon1 = Mon1()
running = True

while running:

    handle_events()
    clear_canvas()
    man.draw()
    mon1.draw()
    mon1.move()

    update_canvas()
    delay(0.05)
