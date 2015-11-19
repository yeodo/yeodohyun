import random
import json
import os
import math

from pico2d import *

from enemy import FirstEnemy
from enemy import SecondEnemy
from map import Map
from player import Player
from missile import Missile
from missile import Enemy_missile
from explosion import Enemy_explosion
from bomb import Bomb
from explosion import Bomb_explosion
from item import Item

import game_framework
import characterselect_state


name = "MainState"

global startspeed
global selectcharacter
global Player_missile
global timer
global score
score = 0

boy = None
map = None
font = None
startspeed = 50

class Timer:
    def __init__(self):
        self.FirstEnemy_timer = 3
        self.SecondEnemy_timer = 49

    def update(self):
        self.FirstEnemy_timer = self.FirstEnemy_timer + 1
        if self.FirstEnemy_timer % 15 == 0:
            enemy = FirstEnemy()
            FirstEnemys.append(enemy)
        if self.FirstEnemy_timer % 30 == 0:
            enemy = FirstEnemy()
            FirstEnemys.append(enemy)

        if self.FirstEnemy_timer >100:
            self.SecondEnemy_timer = self.SecondEnemy_timer + 1

            if self.SecondEnemy_timer % 50== 0:
                enemy = SecondEnemy()
                SecondEnemys.append(enemy)

            for enemy in SecondEnemys:
                if enemy.attacked == 1:
                    if self.SecondEnemy_timer % 2 == 0:
                        if enemy.frame == 1:
                            enemy.frame =0
                            enemy.attacked = 0
                        elif enemy.frame == 0:
                            enemy.frame = 1
                    else:
                        if enemy.frame == 1:
                            enemy.frame =0
                            enemy.attacked = 0
                        elif enemy.frame == 0:
                            enemy.frame = 1

def enter():
    global timer, player, map, Player_missile, FirstEnemys, SecondEnemys, enemy_missile, enemy_explosion, bomb, bomb_explosion, item
    timer = Timer()
    player = Player()
    map = Map()

    bomb = []
    FirstEnemys = []
    SecondEnemys = []
    Player_missile = []
    enemy_missile = []
    enemy_explosion = []
    bomb_explosion = []
    item = []
def exit():
    global timer, player, map, Player_missile, FirstEnemys, SecondEnemys, enemy_missile, enemy_explosion, bomb, bomb_explosion, item
    del(timer)
    del(player)
    del(map)

    del(FirstEnemys)
    del(SecondEnemys)
    del(Player_missile)
    del(enemy_missile)
    del(enemy_explosion)
    del(bomb)
    del(bomb_explosion)
    del(item)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                player.handle_event(event)
                if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and player.state == 1:
                    newmissile = Missile(player.x, player.y)

                    if player.missile_level == 1:
                        newmissile.level = 0
                    if player.missile_level == 2:
                        newmissile.level = 1

                    Player_missile.append(newmissile)
                if event.type == SDL_KEYDOWN and event.key == SDLK_b and player.state == 1:
                    newbomb = Bomb(player.x, player.y)
                    bomb.append(newbomb)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update():
    global score
    timer.update()
    player.update()
    map.update()

    for enemy in FirstEnemys :
        enemy.update()
        enemy.missile = enemy.missile + 1
        if enemy.missile % 25 == 0:
            missile = Enemy_missile(enemy.x, enemy.y-70)
            enemy_missile.append(missile)
        if enemy.y < -50:
            FirstEnemys.remove(enemy)

    for enemy in SecondEnemys :
        enemy.update()
        enemy.missile = enemy.missile + 1
        if enemy.missile % 25 == 0:
            missile = Enemy_missile(enemy.x-15, enemy.y-70)
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x, enemy.y-70)
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x+15, enemy.y-70)
            enemy_missile.append(missile)
        if enemy.y < -50:
            SecondEnemys.remove(enemy)

    for member in Player_missile :
        member.update()
        if member.y > 800:
            Player_missile.remove(member)
    for member in enemy_missile :
        member.update()
        if member.y < -50:
            enemy_missile.remove(member)
    for member in enemy_explosion :
        member.update()
        if member.frame == 10:
            enemy_explosion.remove(member)

    for member in enemy_explosion :
        member.update()
        if member.frame == 10:
            enemy_explosion.remove(member)
    for missile in Player_missile:
        for enemy in FirstEnemys:
            if collide(enemy,missile):
                newexplosion = Enemy_explosion(enemy.x, enemy.y)
                enemy_explosion.append(newexplosion);
                Player_missile.remove(missile)
                FirstEnemys.remove(enemy)
                score += 1

    for missile in Player_missile:
        for enemy in SecondEnemys:
            if collide(enemy,missile):
                enemy.count += player.missile_level
                enemy.attacked = 1
                Player_missile.remove(missile)
                if enemy.count >= 3:
                    SecondEnemys.remove(enemy)
                    score += 3
                    newexplosion = Enemy_explosion(enemy.x, enemy.y)
                    enemy_explosion.append(newexplosion);
                    appearance = random.randint(0, 3)
                    if appearance == 1:
                        newitem = Item(enemy.x, enemy.y)
                        item.append(newitem);


    for member in enemy_explosion:
        if member.frame == 12:
            enemy_explosion.remove(member)

    for member in bomb:
        member.update()
        if member.frame == 12:
            bomb.remove(member)
            newexplosion = Bomb_explosion(member.x, member.y)
            bomb_explosion.append(newexplosion);

    for member in bomb_explosion:
        member.update()
        for enemy in FirstEnemys:
            if member.frame >3:
                if collide(enemy,member):
                    FirstEnemys.remove(enemy)
                    score += 1
        for enemy in SecondEnemys:
            if member.frame >3:
                if collide(enemy,member):
                    SecondEnemys.remove(enemy)
                    score += 3
        for enemy in enemy_missile:
            if member.frame >3:
                if collide(enemy,member):
                    enemy_missile.remove(enemy)

        if member.frame == 12:
            bomb_explosion.remove(member)

    for member in item:
        member.update()
        if collide(player,member):
            item.remove(member)
            player.missile_level = 2

    print ("score %d" %(score))


def draw():
    clear_canvas()
    map.draw()
    player.draw()
    for member in FirstEnemys :
        member.draw()
    for member in SecondEnemys :
        member.draw()
    for member in Player_missile :
        member.draw()
    for member in enemy_missile :
        member.draw()
    for member in enemy_explosion :
        member.draw()
    for member in bomb:
        member.draw()
    for member in bomb_explosion:
        member.draw()
    for member in item:
        member.draw()

    if player.state == 1:
        player.draw_bb()
    for member in FirstEnemys:
        member.draw_bb()
    for member in SecondEnemys:
        member.draw_bb()
    for member in Player_missile:
        member.draw_bb()
    for member in enemy_missile:
        member.draw_bb()
    for member in bomb_explosion:
        member.draw_bb()
    for member in item:
        member.draw_bb()


    update_canvas()