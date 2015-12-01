from pico2d import *

class Bomb:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.angle = 0
        if Bomb.image == None:
            self.image = load_image('resource\\player\\bomb.png')

    def update(self):
        self.frame = self.frame + 1
        self.y+=30;
        if self.angle >0:
            self.x -= 8*math.cos( self.angle * 3.14 / 180)
        elif self.angle <0:
            self.x += 8*math.cos( self.angle * 3.14 / 180)
    def draw(self):
        self.image.clip_draw( self.frame * 16, 0, 16, 32, self.x, self.y )
