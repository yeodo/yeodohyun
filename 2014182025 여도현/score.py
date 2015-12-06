import game_framework
import title_state
from pico2d import *
from ui import UI

from pico2d import *

class Score:
    def __init__(self):
        self.image = load_image('resource\\score.png')
        self.show =0

    def draw(self):
            self.image.clip_draw(0, 0, 500, 750, 250, 375)

    def __del__(self):
        del self.image
