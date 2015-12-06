import game_framework
import title_state
from pico2d import *


global startsound
global sound
sound = 0
name = "StartState"
image = None
logo_time = 0.0
def enter():
    global image
    global sound
    sound = 0
    open_canvas(500,750)
    image = load_image('resource\kpu_credit.png')
def exit():
    global image
    del(image)
    close_canvas()


def update():
    global logo_time
    global sound
    if(sound ==0):
        sound = load_wav('resource\\sound\\gamestart.wav')
        sound.set_volume(30)
        sound.play()
    if(logo_time >2.0):
        sound = load_music('resource\\sound\\bgm.mp3')
        sound.set_volume(40)
        sound.repeat_play()
        logo_time = 0
       # game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time+=0.01


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