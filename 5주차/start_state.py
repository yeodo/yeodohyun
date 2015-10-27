import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(500,750)
    image = load_image('resource\\kpu_credit.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass


def update():
    global logo_time

    if(logo_time >1.0):
        logo_time = 0
       # game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time+=0.01
    pass


def draw():
    global image
    clear_canvas()
    image.draw(250,375)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass