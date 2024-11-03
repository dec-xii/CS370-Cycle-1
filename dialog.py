import pygame as pg


class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.text = ""


class Dialog():
    def __init__(self):
        self.font = pg.font.SysFont('Comic Sans MS', 40)
        self.text = ["This", "is", "a", "test"]
        self.index = 0
        self.visable = True
        self.text_surface = self.font.render(
            self.text[self.index], False, (255, 255, 255))

    def update(self):
        if self.index < len(self.text) - 1:
            self.index += 1
        else:
            self.index = 0
        self.text_surface = self.font.render(
            self.text[self.index], False, (255, 255, 255))

    def display(self, pos, screen):
        if self.visable:
            screen.blit(self.text_surface, pos)
