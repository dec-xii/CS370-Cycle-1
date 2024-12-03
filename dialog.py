import pygame as pg

UI_RECT = pg.Rect(1200, 60, 500, 50)


class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.text = ""


class Dialog():
    def __init__(self):
        # self.font = pg.font.SysFont('Comic Sans MS', 40)
        self.font = pg.font.Font("Assets/SuperPixel-m2L8j.ttf", 30)
        self.text = ["This is a test",
                     "This is where the NPC Dialogue will be displayed"]
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
        self.text_surface.set_clip(UI_RECT)
        # self.text_surface.scroll(-1)

        pg.draw.rect(screen, "green", UI_RECT)
        screen.blit(self.text_surface, UI_RECT.topleft)
