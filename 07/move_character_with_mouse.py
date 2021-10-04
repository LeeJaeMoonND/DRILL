from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global cursorX, cursorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursor
            x, y = x+((event.x-x)/5), y+(((KPU_HEIGHT - 1 - event.y)-y)/5)
            cursorX, cursorY = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png');

hide_cursor()
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cursorX,cursorY = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if cursorX<x :
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    cursor.draw(cursorX, cursorY, 50, 52)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

    handle_events()

close_canvas()




