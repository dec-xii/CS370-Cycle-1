import pygame as pg
from pygame import image
from enum import Enum
import os
from constants import MAIN_PATH


class items(Enum):
    CIGARETTE = 0
    KEYS = 1
    TOOTHBRUSH = 2
    UTENSILS = 3
    BED_SHEETS = 4
    LIGHTER = 5
    POSTER = 6


class dq_object:
    def __init__(self, name, imagePath, width=50, height=50, isUsable=False):
        self.image = pg.transform.scale(
            pg.image.load(os.path.join(MAIN_PATH, imagePath)), (width, height))
        self.width = width
        self.height = height
        self.name = name


class dq_item:
    def __init__(self, dqObject, pos_x, pos_y):
        self.position_x = pos_x
        self.position_y = pos_y
        self.myObject = dqObject
        self.myRect = pg.Rect(pos_x, pos_y, dqObject.width, dqObject.height)

    def render(self, screen):
        screen.blit(self.myObject.image, (self.position_x, self.position_y))

    def check_collision(self, player_rect):
        if player_rect.colliderect(self.myRect):
            return True
        return False


class dq_inventoryItem:
    def __init__(self, dqObject, cnt):
        self.myObject = dqObject
        self.count = cnt

    def action(self):
        if (self.count <= 0):
            return False
        self.count -= 1
        return True
