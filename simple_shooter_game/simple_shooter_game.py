import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((600, 400))


class Sprite:
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.dir = 'stop'
        self.image = pg.image.load(image)
        self.w, self.h = self.image.get_rect().size
        self.update()

    def update(self):
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)


baddy = Sprite('./simplest_game/baddy.png', 0, 10)
bully = Sprite('./simplest_game/bully.png', 260, 295)
goody = Sprite('./simplest_game/goody.png', 250, 325)

loop = 1
while loop:
    screen.fill((0, 0, 0))
    if baddy.x < 600:
        baddy.x += .05
    else:
        baddy.x = -100

    if (bully.dir == 'up'):
        bully.y -= 1
        if bully.rect.colliderect(baddy.rect):
            print("Ouch!")
            bully.y = 295
            bully.dir = 'stop'
        if bully.y < 0:
            bully.y = 295
            bully.dir = 'stop'

    if (goody.dir == 'left') & (goody.x > 0):
        goody.x -= .1
        bully.x -= .1
    if (goody.dir == 'right') & (goody.x < 550):
        goody.x += .1
        bully.x += .1

    screen.blit(baddy.image, (baddy.x, baddy.y))
    screen.blit(bully.image, (bully.x, bully.y))
    screen.blit(goody.image, (goody.x, goody.y))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[K_UP]:
                print("pew!")
                bully.dir = 'up'
            if keys[K_LEFT]:
                goody.dir = 'left'
            if keys[K_RIGHT]:
                goody.dir = 'right'
        if event.type == pg.KEYUP:
            goody.dir = 'stop'
            if bully.dir != 'up':
                bully.dir = 'stop'

    pg.display.update()

pg.quit()
