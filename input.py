import pygame as pg


class Input:
    def __init__(self):
        self.mouse_state = []
        self.old_mouse_state = []
        self.mouse_pos = []
        self.keyboard_state = []

    def is_pressed(self, keycode):
        return self.keyboard_state[keycode]

    def mouseUp(self, button):
        return self.old_mouse_state[button] and not self.mouse_state[button]

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.old_mouse_state = self.mouse_state
        self.mouse_state = pg.mouse.get_pressed(3)
        self.keyboard_state = pg.key.get_pressed()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
