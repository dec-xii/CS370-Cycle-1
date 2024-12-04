import pygame as pg
import os
from constants import MAIN_PATH

UI_RECT = pg.Rect(1200, 60, 500, 50)


class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.text = ""


class Dialog():
    def __init__(self):
        self.font = pg.font.Font(os.path.join(
            MAIN_PATH, "Assets/SuperPixel-m2L8j.ttf"), 30)
        self.text = ["Go get the key!",
                     "Go to the cafe!"]
        self.index = 0
        self.visable = True
        self.text_surface = self.font.render(
            self.text[self.index], False, (255, 255, 255))

    def update(self, inv):
        if self.index < len(self.text) - 1:
            for item in inv.get_item_list():
                if (item.name == "keys"):
                    self.index += 1
        else:
            self.index = 0
        self.text_surface = self.font.render(
            self.text[self.index], False, (255, 255, 255))

    def display(self, pos, screen):
        # self.text_surface.scroll(-2)
        subsurface = UI_RECT.copy()
        subsurface.update((0, 0), subsurface.size)

        pg.draw.rect(screen, "grey", UI_RECT)
        screen.blit(self.text_surface, UI_RECT, subsurface)
