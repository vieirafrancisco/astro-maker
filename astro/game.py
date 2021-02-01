import pygame as pg

from astro.src.sprites import Player

class Game:
    def __init__(self):
        self.running = False
        self.window = None
        self.clock = pg.time.Clock()

    def new(self):
        self.running = True
        self.window = pg.display.set_mode((1280, 768))
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self)
    
    def cleanup(self):
        pg.quit()

    def handle_event(self, event):
        if event.type == pg.QUIT:
            self.running = False

    def render(self):
        self.all_sprites.draw(self.window)

    def update(self):
        self.all_sprites.update()

    def execute(self):
        self.new()
        while self.running:
            for event in pg.event.get():
                self.handle_event(event)
            self.window.fill((0,0,0))
            self.render()
            self.update()
            pg.display.flip()
            self.clock.tick(60)
        self.cleanup()
