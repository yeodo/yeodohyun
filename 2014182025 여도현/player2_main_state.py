import random
import json
import os
import math

from pico2d import *

from enemy import FirstEnemy
from enemy import SecondEnemy
from enemy import Boss
from map import Map
from player import Player
from missile import Missile
from missile import Enemy_missile
from missile import Boss_missile
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
global BoundingBox
global BossAppear
global Bossdie
score = 0
BoundingBox= 0
Bossdie = 0
sound = 0
angle = 0
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

        if self.FirstEnemy_timer >200:
            self.SecondEnemy_timer = self.SecondEnemy_timer + 1

            if self.SecondEnemy_timer % 100== 0:
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
    global timer, player, map, Player_missile, FirstEnemys, SecondEnemys, enemy_missile, enemy_explosion, bomb, bomb_explosion, item, boss, boss_missile
    global angle
    timer = Timer()
    player = Player()
    player.kind = 2
    map = Map()
    map.kind = 2

    bomb = []
    FirstEnemys = []
    SecondEnemys = []
    Player_missile = []
    enemy_missile = []
    enemy_explosion = []
    bomb_explosion = []
    item = []
    boss = []
    boss_missile = [Boss_missile(10,10 ) for i in range(120)]
    for member in boss_missile:
        member.angle = angle
        angle += 8
        if angle >180 :
            angle = 0
def exit():
    global timer, player, map, Player_missile, FirstEnemys, SecondEnemys, enemy_missile, enemy_explosion, bomb, bomb_explosion, item, boss, boss_missile
    del(timer)
    del(player)
    del(map)
    del(boss)

    del(FirstEnemys)
    del(SecondEnemys)
    del(Player_missile)
    del(enemy_missile)
    del(enemy_explosion)
    del(bomb)
    del(bomb_explosion)
    del(item)
    del(boss_missile)

def pause():
    pass


def resume():
    pass


def handle_events():
    global BoundingBox
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
                    player.missile_sound.play()
                    newmissile = Missile(player.x, player.y)
                    if player.missile_level == 1:
                        newmissile.level = 0
                    if player.missile_level == 2:
                        newmissile.level = 1

                    Player_missile.append(newmissile)
                if event.type == SDL_KEYDOWN and event.key == SDLK_b and player.state == 1:
                    newbomb = Bomb(player.x, player.y)
                    newbomb.angle = 3
                    bomb.append(newbomb)
                    newbomb = Bomb(player.x, player.y)
                    newbomb.angle = -3
                    newbomb.angle = -3
                    bomb.append(newbomb)
                if event.type == SDL_KEYDOWN and event.key == SDLK_h and player.state == 1:
                    if BoundingBox == 0:
                        BoundingBox = 1
                    elif BoundingBox == 1:
                        BoundingBox = 0

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
    global BoundingBox
    global sound
    global angle
    global Bossdie
    global player
    if Bossdie == 0:
        timer.update()
    player.update()
    map.update()

    for enemy in FirstEnemys :
        enemy.update()
        enemy.missile = enemy.missile + 1
        if enemy.missile % 20 == 0:
            missile = Enemy_missile(enemy.x, enemy.y-70)
            enemy_missile.append(missile)
            missile.missile_sound.play()
        if enemy.y < 0:
            FirstEnemys.remove(enemy)

    for enemy in SecondEnemys :
        enemy.update()
        enemy.missile = enemy.missile + 1
        if enemy.missile % 30 == 0:
            missile = Enemy_missile(enemy.x-30, enemy.y-50)
            missile.type = 1
            missile.angle = 6
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x-20, enemy.y-60)
            missile.type = 1
            missile.angle = 4
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x-10, enemy.y-70)
            missile.type = 1
            missile.angle = 2
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x-10, enemy.y-70)
            missile.type = 1
            missile.angle = 0
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x, enemy.y-70)
            missile.type = 1
            missile.angle = 0
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x+10, enemy.y-70)
            missile.type = 1
            missile.angle = 0
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x+10, enemy.y-70)
            missile.type = 1
            missile.angle = -2
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x+20, enemy.y-60)
            missile.type = 1
            missile.angle = -4
            enemy_missile.append(missile)
            missile = Enemy_missile(enemy.x+30, enemy.y-50)
            missile.type = 1
            missile.angle = -6
            enemy_missile.append(missile)
            missile.missile_sound.play()
        if enemy.y < 0:
            SecondEnemys.remove(enemy)

    for member in Player_missile :
        member.update()
        if member.y > 800:
            Player_missile.remove(member)
    for member in enemy_missile :
        member.update()
        if member.y < 0:
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
                newexplosion.firstenemy_explosion_sound.play()
                enemy_explosion.append(newexplosion);
                Player_missile.remove(missile)
                FirstEnemys.remove(enemy)
                score += 5

    for missile in Player_missile:
        for enemy in SecondEnemys:
            if collide(enemy,missile):
                enemy.count += player.missile_level
                enemy.attacked = 1
                Player_missile.remove(missile)
                if enemy.count >= 3:
                    SecondEnemys.remove(enemy)
                    score += 10
                    newexplosion = Enemy_explosion(enemy.x, enemy.y)
                    newexplosion.secondenemy_explosion_sound.play()
                    enemy_explosion.append(newexplosion);
                    appearance = random.randint(0, 1)
                    if appearance == 1:
                        newitem = Item(enemy.x, enemy.y)
                        newitem.drop_sound.play()
                        item.append(newitem);


    for member in enemy_explosion:
        if member.frame == 13:
            enemy_explosion.remove(member)

    for member in bomb:
        member.update()
        if member.y > 500:
            bomb.remove(member)
            newexplosion = Bomb_explosion(member.x, member.y)
            newexplosion.explosion_sound.play()
            bomb_explosion.append(newexplosion)

    for member in bomb_explosion:
        member.update()
        for enemy in FirstEnemys:
            if member.frame >3:
                if collide(enemy,member):
                    FirstEnemys.remove(enemy)
                    score += 5
        for enemy in SecondEnemys:
            if member.frame >3:
                if collide(enemy,member):
                    SecondEnemys.remove(enemy)
                    score += 10
        for enemy in enemy_missile:
            if member.frame >3:
                if collide(enemy,member):
                    enemy_missile.remove(enemy)
        for missile in boss_missile:
            missile.update()
            if collide(missile,member):
                missile.x, missile.y = 250, 600
                missile.type = random.randint(1, 3)

        if member.frame == 12:
            bomb_explosion.remove(member)

    for member in item:
        member.update()
        if collide(player,member):
            player.get_sound.play()
            item.remove(member)
            player.missile_level = 2
            player.missile_sound = load_wav('resource\\sound\\player_missile_level2.ogg')
            player.missile_sound.set_volume(60)
    if score == 210 or score == 205:
        newBoss = Boss()
        boss.append(newBoss)
        for member in boss:
            if member.appear == 0:
                member.appear_sound.play()
                member.sound.repeat_play()
                member.appear = 1
                score +=1
    for member in boss:
        member.update()
        if member.appear == 1:
            if member.y <= 650:
                for missile in boss_missile:
                    missile.update()
                    if missile.x < 0 or missile.x > 600 or missile.y<0 or missile.y > 800:
                        missile.x, missile.y = 250, 600
                        missile.type = random.randint(1, 3)

    for member in boss:
        for missile in Player_missile:
            if member.y <= 650:
                if collide(missile,member):
                    newexplosion = Enemy_explosion(missile.x, missile.y)
                    newexplosion.firstenemy_explosion_sound.play()
                    enemy_explosion.append(newexplosion);
                    Player_missile.remove(missile)
                    member.life -= player.missile_level
                    print ("boss %d" %(member.life))
        for explosion in bomb_explosion:
            if collide(member,explosion):
                member.life -= 1
    for member in boss:
        if member.life <= 0 :
            for enemy in FirstEnemys:
                FirstEnemys.remove(enemy)
            for enemy in SecondEnemys:
                SecondEnemys.remove(enemy)
            for missile in enemy_missile:
                enemy_missile.remove(missile)
            for missile in boss_missile:
                boss_missile.remove(missile)
            for missile in Player_missile:
                Player_missile.remove(missile)
            Bossdie = 1
            boss.remove(member)

    if player.state == 1:
        for missile in boss_missile:
            if collide(missile,player):
                boss_missile.remove(missile)
                newexplosion = Enemy_explosion(missile.x, missile.y)
                newexplosion.firstenemy_explosion_sound.play()
                enemy_explosion.append(newexplosion);

        for missile in enemy_missile:
            if collide(missile,player):
                enemy_missile.remove(missile)
                newexplosion = Enemy_explosion(missile.x, missile.y)
                newexplosion.firstenemy_explosion_sound.play()
                enemy_explosion.append(newexplosion);

    print ("score %d" %(score))
def draw():
    global BoundingBox
    clear_canvas()

    map.draw()
    player.draw()
    for member in boss:
        member.draw()
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
    for member in boss:
        if member.y == 650:
            for member in boss_missile:
                member.draw()

    if BoundingBox == 1:
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
        for member in boss:
            member.draw_bb()
        for member in boss:
            if member.appear == 1:
                for member in boss_missile:
                    member.draw_bb()


    update_canvas()
