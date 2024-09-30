import pygame as pg
import sprites

fps = 60


def movement(x):
    # x.rect[0] = x.rect[0] + 1
    # x.rect[1] = x.rect[1] + 1
    return x


class Game:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((1920, 1080))
        self.clock = pg.time.Clock()
        self.deltaTime = 0

        self.player = sprites.Sprite("Knight.png", [0, 0], [
                                     32, 32], 13, 1, controller=movement)
        self.sprites = pg.sprite.RenderPlain(self.player)

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def update(self):
        self.player.update(self.deltaTime)
        self.deltaTime = self.clock.tick(fps) / 1000

    def render(self):
        self.screen.fill("black")
        self.sprites.draw(self.screen)
        pg.display.flip()

    def clean(self):
        pg.quit()
