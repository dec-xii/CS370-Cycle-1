import pygame as pg


class Sprite(pg.sprite.Sprite):
    def __init__(self, color, width, height, moveFunc):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.move = moveFunc

    def update(self):
        if self.move:
            self = self.move(self)
