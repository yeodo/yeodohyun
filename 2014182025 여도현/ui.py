
from pico2d import *
__author__ = 'dohyun'

class UI:
    def __init__(self):
        self.score = 0
        self.bomb = 0
        self.playerlife = 2
        self.kind = 0
        self.font=load_font('resource\\ConsolaMalgun.TTF', 20 )
        self.scorefont=load_font('resource\\ConsolaMalgun.TTF', 60 )
        self.time = 0.0
    def update(self):
        self.time = get_time()

    def draw(self):
        if self.kind == 0:
            self.font.draw(380,730,'SCORE %d ' %(self.score ))
            self.font.draw(20,20,'BOMB %d  LIFE %d' %(self.bomb , self.playerlife ))
        if self.kind == 1:
            self.scorefont.draw(180,350,'SCORE %d ' %(self.score ))
            self.font.draw(180,300,'Restart : Space Bar')
            self.font.draw(180,270,'End : Esc')


def test_ui():
    open_canvas()
    ui = UI()
    for i in range(100):
        ui.score = i
        clear_canvas()
        ui.draw()
        update_canvas()

    delay(2)
    close_canvas()

if __name__ == '__main__':
    test_ui()
