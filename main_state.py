import random
import json
import os

from pico2d import *

import game_framework
import characterselect_state



name = "MainState"

global state  # 0일 때 등장애니메이션 1일 때 이동애니메이션
global mapmove
global startspeed
global selectcharacter
state = 0
boy = None
map = None
font = None
startspeed = 50



class Map:
    def __init__(self):
        self.image = load_image('map.png')
        self.x, self.y = 0,0
    def update(self):
        global startspeed
        if state == 0 :
            if self.y < 400:
                self.y += startspeed
                startspeed = startspeed - 3
            else:
                self.y = 0
        else :
            if self.y < 400:
                self.y += 20
            else:
                self.y = 20

    def draw(self):
        self.image.clip_draw(0, 0, 500, 750 + self.y, 250, 375)



class Player:
    def __init__(self):
        if state == 0:
            self.x, self.y = 250, 0
            self.frame = 0
            self.image = load_image('player1_appear_animation.png')
            self.dir = 1

    def update(self):
        global state
        if state == 0:
            if self.frame < 10:
                self.frame = self.frame + 1
                self.y += 10
            else:
                state = 1
                self.x, self.y = 250, 200
                self.frame = 6
                self.image = load_image('player1_animation.png')
                self.dir = 1
        if state == 1:
            if self.frame % 2 == 0:
                self.frame = self.frame + 1
            elif self.frame % 2 == 1:
                self.frame = self.frame - 1
        delay(0.07)

    def draw(self):
        if state == 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 250, self.x, self.y)
        elif state == 1:
            self.image.clip_draw(self.frame * 50, 0, 50, 70, self.x, self.y)


def enter():
    global player, map
    player = Player()
    map = Map()
def exit():
    global player, map
    del(player)
    del(map)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.key == SDLK_RIGHT:
            player.x += 10
            if player.frame < 13:
                player.frame = player.frame + 1
        elif event.key == SDLK_LEFT:
            player.x -= 10;
            if player.frame > 0:
                player.frame = player.frame - 1



def update():
    player.update()
    map.update()


def draw():
    clear_canvas()
    map.draw()
    player.draw()
    update_canvas()





