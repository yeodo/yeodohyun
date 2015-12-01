import game_framework
import characterselect_state
from pico2d import *

name = "TitleState"
image = None
pushspace = 0
def enter():
    global image
    global music
    global pushspace

    image = load_image('resource\\title.png')
    pushspace = load_wav('resource\\sound\\pushspace.ogg')
    pushspace.set_volume(100)

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
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                pushspace.play()
                delay(0.5)
                game_framework.change_state(characterselect_state)


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
