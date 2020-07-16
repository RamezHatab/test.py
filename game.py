import pygame as pg
import random
import settings
import player

class Game:
    def __init__(self):
        #initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pg.display.set_caption("Platformer")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.player = player.Player(self)
        self.all_sprites.add(self.player)
        for plat in settings.PLATFORM_LIST:
            p = player.Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        p_ground = player.Platform(*settings.GROUND_PLATFORM)
        self.all_sprites.add(p_ground)
        self.ground.add(p_ground)
        self.run()

    def run(self):
        
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop update
        if self.player.pos.x + settings.IMG_WIDTH / 2 > settings.WIDTH:
            self.player.set_spawn()
            for plat in self.platforms:
                plat.kill()
            for plat in settings.CREATE_PLATFORMS():
                p = player.Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False) 
        ground_hits = pg.sprite.spritecollide(self.player, self.ground, False)
        if hits:
            if self.player.vel.y > 0:
                self.player.rect.bottom = hits[0].rect.top + 1
                self.player.vel.y = 0
            elif self.player.vel.y < 0:
                self.player.rect.top = hits[0].rect.bottom - 1
                self.player.vel.y = 0
            self.player.pos.y = self.player.rect.bottom
        if ground_hits:
            self.player.set_spawn()
        #if self.player.rect.right >= 0:
            #if self.player.vel.x != 0:
                #self.player.pos.x += abs(self.player.vel.x)
            '''for plat in self.platforms:
                    plat.rect.x -= self.player.vel.x
                    if plat.rect.right <= 0:
                        plat.kill()'''
                     
            
    def events(self):
        #game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()


    def draw(self):
        #game loop - draw
        self.screen.fill(settings.SKY_BLUE)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_start_screen(self):
        #game start screen
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()