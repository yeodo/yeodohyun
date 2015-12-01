import random
from pico2d import *

class Item:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.xmove = 0
        self.ymove = 0
        if Item.image == None:
            self.image = load_image('resource\\item.png')
        self.drop_sound = load_wav('resource\\sound\\item_drop.wav')
        self.drop_sound.set_volume(70)
    def update(self):
        self.frame += 1
        if self.frame == 12:
            self.frame = 0

        if self.xmove == 0:
            self.x += random.randint(10, 30)
            if self.x > 475:
                self.xmove = 1
        elif self.xmove == 1:
            self.x -= random.randint(10, 30)
            if self.x < 25:
                self.xmove = 0

        if self.ymove == 0:
            self.y += random.randint(10, 30)
            if self.y > 725:
                self.ymove = 1
        elif self.xmove == 1:
            self.y -= random.randint(10, 30)
            if self.y < 25:
                self.ymove = 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 25, self.y - 25 , self.x + 25, self.y + 25

    def draw(self):
        self.image.clip_draw( self.frame * 50, 0, 50, 50, self.x, self.y )
