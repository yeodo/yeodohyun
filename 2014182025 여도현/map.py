from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('resource\\background\\map1.png')
        self.kind = 0
        self.x, self.y = 0,0
    def update(self):
        if self.kind == 1:
            self.image = load_image('resource\\background\\map1.png')
            if self.y < 400:
                self.y += 10
            else:
                self.y = 20
        elif self.kind == 2:
            self.image = load_image('resource\\background\\map2.png')
            if self.y < 750:
                self.y += 10
            else:
                self.y = 0
        elif self.kind == 3:
            self.image = load_image('resource\\score.png')

    def draw(self):
        if self.kind == 1:
            self.image.clip_draw(0, 0, 500, 750 + self.y, 250, 375)
        if self.kind == 2:
            self.image.clip_draw(0, 0, 500, 750 + self.y, 250, 375)
        if self.kind == 3:
            self.image.clip_draw(0, 0, 500, 750 + self.y, 250, 375)

    def __del__(self):
        del self.image
