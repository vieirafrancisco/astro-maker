import pygame as pg

vector = pg.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites]
        pg.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.image = pg.Surface((64, 64))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.pos = vector(100, 100)
        self.rect.topleft = self.pos
        self.acc = vector(0, 0)
        self.vel = vector(0, 0)

    def update(self):
        self.move()
        if self.rect.bottomright[1] < 768:
            self.acc = vector(0, 1) * 0.2 # gravity
        else:
            self.acc *= 0
            self.vel *= 0
            self.pos = (self.pos.x, 704)
        self.vel += self.acc
        self.pos += self.vel
        self.rect.topleft = self.pos

    def move(self):
        dx, dy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            dx -= 5
        if keys[pg.K_RIGHT]:
            dx += 5
        self.pos += (dx, dy)
