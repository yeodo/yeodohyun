from pico2d import *

class Enemy_explosion:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        if Enemy_explosion.image == None:
            self.image = load_image('resource\\Enemy\\Enemy1_explosion.png')
        self.firstenemy_explosion_sound = load_wav('resource\\sound\\firstenemy_death.ogg')
        self.firstenemy_explosion_sound.set_volume(80)
        self.secondenemy_explosion_sound = load_wav('resource\\sound\\secondenemy_death.ogg')
        self.secondenemy_explosion_sound.set_volume(90)

    def update(self):
        self.frame = self.frame + 1
    def draw(self):
        self.image.clip_draw( self.frame * 80, 0, 80, 80, self.x, self.y )


class Bomb_explosion:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        if Bomb_explosion.image == None:
            self.image = load_image('resource\\player\\bomb_explosion.png')
        self.explosion_sound = load_wav('resource\\sound\\bomb.ogg')
        self.explosion_sound.set_volume(120)
    def update(self):
        self.frame = self.frame + 1


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 150, self.y - 150 , self.x + 150, self.y + 150
    def draw(self):
        self.image.clip_draw( self.frame *308, 0, 308, 304, self.x, self.y )
