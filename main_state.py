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
                self.move = 0   # 0이면 정지 1이면 오른쪽 2면 왼쪽
                self.frame = 6
                self.image = load_image('player1_animation.png')
                self.dir = 1
        if state == 1:
            if self.move == 0 :
                if self.frame % 2 == 0:
                    self.frame = self.frame + 1
                elif self.frame % 2 == 1:
                    self.frame = self.frame - 1
            if self.move == 1 :
                if self.x < 470:
                    self.x += 10
                if self.frame < 13:
                    self.frame = self.frame + 1
            if self.move == 2:
                if self.x > 30:
                   self.x -= 10;
                if self.frame > 0:
                    self.frame = self.frame - 1
            if self.move == 3 :
                if self.y < 650:
                    self.y += 10
            if self.move == 4:
                if self.y > 50:
                    self.y -= 10;
        delay(0.07)

    def draw(self):
        if state == 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 250, self.x, self.y)
        elif state == 1:
            self.image.clip_draw(self.frame * 50, 0, 50, 70, self.x, self.y)

class Enemy1:
    def __init__(self):
            self.x, self.y = 250, 800
            self.frame = 3
            self.image = load_image('Enemy_1.png')
            self.dir = 1

    def update(self):
        if state == 1:
            self.y -= 15


    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 95, self.x, self.y)


def enter():
    global player, map, enemy1
    player = Player()
    map = Map()
    enemy1 = Enemy1()
def exit():
    global player, map, enemy1
    del(player)
    del(map)
    del(enemy1)

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
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            player.move = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            player.move = 2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            player.move = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            player.move = 4
        if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            if player.move == 1:
                player.move = 0
            player.frame = 6
        if event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            if player.move == 2:
                player.move = 0
            player.frame = 6
        if event.type == SDL_KEYUP and event.key == SDLK_UP:
            if player.move == 3:
                player.move = 0
            player.frame = 6
        if event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            if player.move == 4:
                player.move = 0
            player.frame = 6
            #여기까지 캐릭터 이동



def update():
    player.update()
    map.update()
    enemy1.update()


def draw():
    clear_canvas()
    map.draw()
    player.draw()
    enemy1.draw()
    update_canvas()