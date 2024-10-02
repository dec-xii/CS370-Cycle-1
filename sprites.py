import pygame as pg
import os

fps = 60


class Sprite(pg.sprite.Sprite):
    def __init__(self, sheet=None, start=[0, 0], size=[0, 0], columns=0, rows=0, controller=None):
        # Call parent constructor
        pg.sprite.Sprite.__init__(self)

        # Load sprite
        if os.path.exists(sheet):
            # Load spritesheet
            self.images = self.load_sheet(pg.image.load(
                sheet).convert_alpha(), start, size, columns, rows)
            self.animated = True
            self.image = self.images[0]
        else:
            # Load blank rectangle
            self.image = pg.Surface([100, 100])
            self.image.fill("Purple")
            self.animated = False

        # Animation
        if self.animated:
            self.frame = 0
            self.frame_timer = 0
            self.deltaTime = 0

        # Movement
        self.velocity = [0, 0]
        # Set self.rect as a pygame.Rect object using start and size
        self.rect = pg.Rect(start[0], start[1], size[0], size[1])
        self.move = controller

    # Load spritesheets
    def load_sheet(self, sheet, start, size, columns, rows=1):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames

    def update(self, deltaTime, input):
        # Update the sprite location
        if self.move:
            self = self.move(self, input)
        if self.animated:
            self.next_frame(deltaTime)

    def next_frame(self, deltaTime):
        # Update frame fps interval
        if self.frame_timer > fps / 6:
            if self.frame < len(self.images) - 1:
                self.frame += 1
            else:
                self.frame = 0
            self.frame_timer = 0
        else:
            self.frame_timer += deltaTime * 100
        self.image = pg.transform.scale_by(self.images[self.frame], 5)
