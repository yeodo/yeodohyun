from pico2d import *

class Player:
    def __init__(self):
        self.kind = 0
        self.x, self.y = 250, 0
        self.frame = 0
        if self.kind == 1:
            self.image = load_image('resource\\player\\player1_appear_animation.png')
        if self.kind == 2:
            self.image = load_image('resource\\player\\player2_appear_animation.png')
        self.pos = 0
        self.state = 0      # 0일 때 등장애니메이션 1일 때 이동애니
        self.missile_level = 1
        self.hit = 0
        self.missile_sound = load_wav('resource\\sound\\player_missile_level1.ogg')
        self.missile_sound.set_volume(60)
        self.get_sound = load_wav('resource\\sound\\item_get.wav')
        self.get_sound.set_volume(70)

    def update(self):
        if self.state == 0:
            if self.kind == 1:
                self.image = load_image('resource\\player\\player1_appear_animation.png')
            if self.kind == 2:
                self.image = load_image('resource\\player\\player2_appear_animation.png')
            if self.pos == 0:
                self.frame = 0
                self.x, self.y = 250, 0
                self.pos = 1
            if self.frame < 10:
                self.frame = self.frame + 1
                self.y += 10
            else:
                self.state = 1
                self.x, self.y = 250, 200
                self.LeftAndRight = 0   # 0이면 정지 1이면 오른쪽 2면 왼쪽
                self.UpAndDown = 0   # 0이면 정지 1이면 오른쪽 2면 왼쪽
                self.frame = 6
                if self.kind == 1:
                    self.image = load_image('resource\\player\\player1_animation.png')
                if self.kind == 2:
                    self.image = load_image('resource\\player\\player2_animation.png')
        if self.state == 1:
            if self.LeftAndRight == 0 :
                if self.frame % 2 == 0:
                    self.frame = self.frame + 1
                elif self.frame % 2 == 1:
                    self.frame = self.frame - 1
            if self.LeftAndRight == 1 :
                if self.x < 470:
                    self.x += 15
                if self.frame < 13:
                    self.frame = self.frame + 1
            if self.LeftAndRight == 2:
                if self.x > 30:
                   self.x -= 15
                if self.frame > 0:
                    self.frame = self.frame - 1
            if self.UpAndDown == 1:
                if self.y < 650:
                    self.y += 10
            if self.UpAndDown == 2:
                if self.y > 50:
                    self.y -= 10
        if self.state == 2:
            if self.LeftAndRight == 0 :
                if self.frame % 2 == 0:
                    self.frame = self.frame + 1
                elif self.frame % 2 == 1:
                    self.frame = self.frame - 1
            if self.LeftAndRight == 1 :
                if self.x < 470:
                    self.x += 15
                if self.frame < 13:
                    self.frame = self.frame + 1
            if self.LeftAndRight == 2:
                if self.x > 30:
                   self.x -= 15
                if self.frame > 0:
                    self.frame = self.frame - 1
            if self.UpAndDown == 1:
                if self.y < 650:
                    self.y += 10
            if self.UpAndDown == 2:
                if self.y > 50:
                    self.y -= 10

            self.hit +=1
            if self.hit == 20:
                self.state = 1
                self.hit = 0
                self.image = load_image('resource\\player\\player1_animation.png')
            print('hit %d' %self.hit)

        delay(0.07)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 15, self.y - 25 , self.x + 13, self.y + 25

    def draw(self):
        if self.state == 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 250, self.x, self.y)
        elif self.state != 0:
            self.image.clip_draw(self.frame * 50, 0, 50, 70, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.LeftAndRight = 1
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.LeftAndRight = 2
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.UpAndDown = 1
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.UpAndDown = 2
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.LeftAndRight == 1:
                self.LeftAndRight = 0
            self.frame = 6
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.LeftAndRight == 2:
                self.LeftAndRight = 0
            self.frame = 6
        if (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.UpAndDown == 1:
                self.UpAndDown = 0
        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.UpAndDown == 2:
                self.UpAndDown = 0
            #여기까지 캐릭터 이동