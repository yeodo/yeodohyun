from pico2d import *
import random

class Missile:
    def __init__(self, x, y):
            self.x, self.y = x, y+20
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
            self.image.clip_draw(self.frame * 40, 50, 40, 50, self.x, self.y)
        if self.level == 1:
            self.image.clip_draw(self.frame * 40, 0, 40, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        if self.level == 0:
            return self.x - 10, self.y - 25 , self.x + 10, self.y + 25
        if self.level == 1:
            return self.x - 13, self.y - 25 , self.x + 13, self.y + 25


class Enemy_missile:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y + 40
        self.type = 0
        self.angle = 0
        if Enemy_missile.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_missile.png')
        self.missile_sound = load_wav('resource\\sound\\missile_sound.ogg')
        self.missile_sound.set_volume(80)

    def update(self):
        self.y -= 30
        if self.type == 1:
            if self.angle == 0:
                self.y -= 5
            elif self.angle >0:
                self.x -= 5*math.cos( self.angle * 3.14 / 180)
                self.y -= 5*math.sin( self.angle * 3.14 / 180)
            elif self.angle <0:
                self.x += 5*math.cos( self.angle * 3.14 / 180)
                self.y += 5*math.sin( self.angle * 3.14 / 180)
    def draw(self):
        self.image.clip_draw(0, 0, 31, 31, self.x, self.y )

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 5, self.y - 15 , self.x + 5, self.y + 15

class Boss_missile:
    image = None
    def __init__(self, x, y):
        self.x, self.y = 250, 600
        self.type = 1
        self.angle = 0
        if Enemy_missile.image == None:
            self.image = load_image('resource\\Enemy\\boss_missile.png')
        self.missile_sound = load_wav('resource\\sound\\missile_sound.ogg')
        self.missile_sound.set_volume(60)

    def update(self):
        if self.type == 1:
            self.x -= 20*math.cos( self.angle * 3.14 / 180)
            self.y -= 20*math.sin( self.angle * 3.14 / 180)
        if self.type == 3:
            self.x -= 15*math.cos( self.angle * 3.14 / 180)
            self.y -= 20*math.sin( self.angle * 3.14 / 180)
        if self.type == 2:
            self.x -= 20*math.cos( self.angle * 3.14 / 180)
            self.y -= 10*math.sin( self.angle * 3.14 / 180)
    def draw(self):
        self.image.clip_draw(0, 0, 18, 18, self.x, self.y )

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 7, self.y - 7 , self.x + 7, self.y + 7