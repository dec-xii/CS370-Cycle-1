import pygame as pg


class Input:
    def __init__(self):
        self.mouse_state = []
        self.mouse_pos = []
        self.keyboard_state = []

    def is_pressed(self, keycode):
        return self.keyboard_state[keycode]

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_state = pg.mouse.get_pressed(3)
        self.keyboard_state = pg.key.get_pressed()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
