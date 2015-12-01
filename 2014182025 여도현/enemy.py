import random
from pico2d import *
from missile import Enemy_missile

class FirstEnemy:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(30, 470), random.randint(750, 800)
        self.frame = 3
        self.missile = random.randint(0, 30)
        if FirstEnemy.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_1.png')
    def update(self):
        self.y -= 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 25, self.y - 30 , self.x + 25, self.y + 30
    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 95, self.x, self.y)

class SecondEnemy:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(30, 470), random.randint(750, 800)
        self.frame = 0
        self.count = 0
        self.missile = random.randint(0, 30)
        self.attacked = 0
        if SecondEnemy.image == None:
            self.image = load_image('resource\\Enemy\\Enemy_2.png')
    def update(self):
        self.y -= 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 55, self.y - 40 , self.x + 55, self.y + 40
    def draw(self):
        self.image.clip_draw(0+(self.frame*117), 0, 117, 100, self.x, self.y)

class Boss:
    image = None
    def __init__(self):
        self.x, self.y = 250, 870
        self.missile = 0
        self.attacked = 0
        self.appear_sound = load_wav('resource\\sound\\boss_appear.wav')
        self.appear_sound.set_volume(100)
        self.sound = load_music('resource\\sound\\boss.mp3')
        self.sound.set_volume(120)
        self.appear = 0
        self.life = 100
        self.timer = 0

        if SecondEnemy.image == None:
            self.image = load_image('resource\\Enemy\\boss.png')
    def update(self):
        if self.appear == 1:
            if self.y > 650:
                self.y -= 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
            return self.x - 200, self.y - 20, self.x + 200, self.y + 80
    def draw(self):
        self.image.clip_draw(0, 0, 400, 225, self.x, self.y)
