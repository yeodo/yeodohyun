import game_framework
import title_state
from pico2d import *
from ui import UI

name = "ScoreState"
image = None
def enter():
    global image

    image = load_image('resource\\score.png')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    clear_canvas()
    image.draw(250,375)
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass
