import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites]
        pg.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.image = pg.Surface((64, 64))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)

    def update(self):
        pass
