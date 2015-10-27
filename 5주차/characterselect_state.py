import game_framework
import title_state
import main_state
from pico2d import *


name = "CharacterSelectState"
global select
select = 0
class Background:
     def __init__(self):
        self.image = load_image('resource\\characterselect.png')
     def draw(self):
        self.image.clip_draw(0, 0, 500, 750, 250, 375)

class Aim:
    def __init__(self):
        self.image = load_image('resource\\characterselect_aim.png')
    def draw(self):
        self.image.clip_draw(0, 0, 70, 100, 47 + (73 * select), 45)

def enter():
    global background, aim
    background = Background()
    aim = Aim()


def exit():
    global background, aim
    del(background)
    del(aim)


def handle_events():
    events = get_events()
    global select
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if(select == 1):
                    select = 0
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if(select == 0) :
                    select = 1


def draw():
    clear_canvas()
    background.draw()
    aim.draw()
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass