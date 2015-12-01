import game_framework
import title_state
import player1_main_state
import player2_main_state
from pico2d import *

name = "CharacterSelectState"
global select
global selectsound, selectmovesound
selectsound = 0
selectmovesound = 0
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
    global selectsound, selectmovesound
    selectmovesound = load_wav('resource\\sound\\selectmove.ogg')
    selectmovesound.set_volume(70)
    selectsound = load_wav('resource\\sound\\characterselect.ogg')
    selectsound.set_volume(100)
    background = Background()

    aim = Aim()


def exit():
    global background, aim
    global selectsound, selectmovesound
    del(background)
    del(aim)
    del(selectsound)
    del(selectmovesound)


def handle_events():
    events = get_events()
    global select
    global selectsound, selectmovesound
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                selectsound.play()
                delay(0.7)
                if select == 0:
                    game_framework.change_state(player1_main_state)
                elif select == 1:
                    game_framework.change_state(player2_main_state)
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if(select == 1):
                    select = 0
                    selectmovesound.play()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if(select == 0) :
                    select = 1
                    selectmovesound.play()


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