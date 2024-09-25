import pygame as pg


class Game:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((1920, 1080))
        self.clock = pg.time.Clock()
        pg.draw.circle(self.screen, "red", (500, 500), 40)

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        pg.display.flip()

    def clean(self):
        pg.quit()
