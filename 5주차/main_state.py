import random
import json
import os

from pico2d import *

import game_framework
import characterselect_state



name = "MainState"

global state  # 0일 때 등장애니메이션 1일 때 이동애니
global startspeed
global selectcharacter
global Enemy1
global player_missile
global timer
state = 0
boy = None
map = None
font = None
startspeed = 50

class Timer:
    def __init__(self):
        self.Enemy_timer = 3
        self.Enemy2_timer = 49

    def update(self):
        self.Enemy_timer = self.Enemy_timer + 1
        if self.Enemy_timer % 15 == 0:
            enemy = Enemy1()
            enemy1s.append(enemy)
        if self.Enemy_timer % 30 == 0:
            enemy = Enemy1()
            enemy1s.append(enemy)

        if self.Enemy_timer >100:
            self.Enemy2_timer = self.Enemy2_timer + 1

            if self.Enemy2_timer % 50== 0:
                enemy = Enemy2()
                enemy2s.append(enemy)




class Map:
    def __init__(self):
        self.image = load_image('resource\\background\\map1.png')
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
            self.image = load_image('resource\\player\\player1_appear_animation.png')
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
                self.image = load_image('resource\\player\\player1_animation.png')
                self.dir = 1
        if state == 1:
            if self.move == 0 :
                if self.frame % 2 == 0:
                    self.frame = self.frame + 1
                elif self.frame % 2 == 1:
                    self.frame = self.frame - 1
            if self.move == 1 :
                if self.x < 470:
                    self.x += 15
                if self.frame < 13:
                    self.frame = self.frame + 1
            if self.move == 2:
                if self.x > 30:
                   self.x -= 15
                if self.frame > 0:
                    self.frame = self.frame - 1
            if self.move == 3 :
                if self.y < 650:
                    self.y += 10
            if self.move == 4:
                if self.y > 50:
                    self.y -= 10
        delay(0.07)

    def draw(self):
        if state == 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 250, self.x, self.y)
        elif state == 1:
            self.image.clip_draw(self.frame * 50, 0, 50, 70, self.x, self.y)

class Missile:
    def __init__(self, x, y):
            self.x, self.y = x, y
            self.level = 0
            self.frame = 0
            self.image = load_image('resource\\player\\player_missile.png')

    def update(self):
        self.y += 20
        self.frame = self.frame + 1
        if self.frame > 3:
            self.frame = 0

    def draw(self):
        if self.level == 0:
            self.image.clip_draw(self.frame * 40, 50, 40, 50, self.x, self.y+20)
        if self.level == 1:
            self.image.clip_draw(self.frame * 40, 0, 40, 50, self.x, self.y+20)

class Enemy1:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(30, 470), 800
        self.frame = 3
        self.missile = 0
        if Enemy1.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_1.png')

    def update(self):
        if state == 1:
            self.y -= 10
            for enemy1 in enemy1s:
                if enemy1.y < -50:
                    enemy1s.remove(enemy1)
        self.missile = self.missile + 1
        if self.missile % 25 == 0:
            missile = Enemy_missile(self.x, self.y-70)
            enemy_missile.append(missile)



    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 95, self.x, self.y)

class Enemy2:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(30, 470), 800
        self.frame = 3
        self.count = 0
        self.missile = 0
        if Enemy2.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_2.png')

    def update(self):
        if state == 1:
            self.y -= 10
            for enemy2 in enemy2s:
                if enemy2.y < -50:
                    enemy2s.remove(enemy2)
        self.missile = self.missile + 1
        if self.missile % 25 == 0:
            missile = Enemy_missile(self.x-15, self.y-70)
            enemy_missile.append(missile)
            missile = Enemy_missile(self.x, self.y-70)
            enemy_missile.append(missile)
            missile = Enemy_missile(self.x+15, self.y-70)
            enemy_missile.append(missile)



    def draw(self):
        self.image.clip_draw(0, 0, 117, 99, self.x, self.y)

class Enemy_missile:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.level = 1
        if Enemy_missile.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_missile.png')

    def update(self):
        self.y -= 20

    def draw(self):
        self.image.clip_draw(0, 0, 31, 31, self.x, self.y + 40 )


def enter():
    global timer, player, map, player_missile, enemy1s, enemy2s, enemy_missile
    timer = Timer()
    player = Player()
    map = Map()

    enemy1s = []
    enemy2s = []
    player_missile = []
    enemy_missile = []
def exit():
    global timer, player, map, player_missile, enemy1s, enemy2s, enemy_missile
    del(timer)
    del(player)
    del(map)

    del(enemy1s)
    del(enemy2s)
    del(player_missile)
    del(enemy_missile)

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
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and state == 1:
            newmissile = Missile(player.x, player.y)
            player_missile.append(newmissile)


def update():
    timer.update()
    player.update()
    map.update()
    for enemy1 in enemy1s :
        enemy1.update()
    for enemy2 in enemy2s :
        enemy2.update()
    for member in player_missile :
        member.update()
    for member in enemy_missile :
        member.update()

    for missile in player_missile:
        for enemy in enemy1s:
            if missile.y > enemy.y - 30 and missile.y < enemy.y + 30 and missile.x > enemy.x-20 and missile.x < enemy.x + 20 :
                enemy1s.remove(enemy)
                player_missile.remove(missile)

    for missile in player_missile:
        for enemy2 in enemy2s:
            if missile.y > enemy2.y - 50 and missile.y < enemy2.y + 50 and missile.x > enemy2.x - 55 and missile.x < enemy2.x + 55 :
                enemy2.count += 1
                player_missile.remove(missile)
                if enemy2.count == 3:
                    enemy2s.remove(enemy2)
                    for member in player_missile :
                        member.level = 1



def draw():
    clear_canvas()
    map.draw()
    player.draw()
    for member in enemy1s :
        member.draw()
    for member in enemy2s :
        member.draw()
    for member in player_missile :
        member.draw()
    for member in enemy_missile :
        member.draw()
    update_canvas()