import pygame as pg
import sys
import os
import settings
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    screen = pg.display.set_mode((1000, 800))
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        #self.image = screen.blit("TurqMan1.png")
        '''hg = pg.image.load('TurqMan1.png')
        hgbox = pg.Rect(0, 13, 36, 72)
        self.image = pg.Surface.blit("TurqMan1.png", (300,300), 50)'''
        self.game = game
        self.image = pg.Surface((settings.IMG_WIDTH, settings.IMG_HEIGHT))
        self.image.fill(settings.RED)
        self.rect = self.image.get_rect()
        self.set_spawn()
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def set_spawn(self):
        self.rect.center = (settings.IMG_WIDTH / 2, settings.HEIGHT / 2)
        self.pos = vec(settings.IMG_WIDTH / 2, settings.HEIGHT / 2)

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        ground_hits = pg.sprite.spritecollide(self, self.game.ground, False)
        self.rect.y -= 1
       
        if hits or ground_hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, settings.PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -settings.PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = settings.PLAYER_ACC
        if keys[pg.K_LSHIFT]:
            self.acc.x = settings.PLAYER_ACC * 1.5
        self.acc.x += self.vel.x * settings.PLAYER_FRICTION
        self.vel += self.acc
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        self.pos.x += self.vel.x
        if self.pos.x - settings.IMG_WIDTH / 2 > settings.WIDTH:
            self.pos.x = settings.IMG_WIDTH / 2
        
        self.rect.midbottom = self.pos
        #self.rect.x = self.ret.ccenterx
   
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y