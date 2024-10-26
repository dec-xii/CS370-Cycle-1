
import pygame as pg
from enum import Enum
import sprites


class States(Enum):
    IDLE = 0
    WALK = 1
    ATK = 2


def pointToPoint(x, input):
    if x.rect.center == x.points[x.target]:
        if x.target == len(x.points) - 1:
            x.target = 0
        else:
            x.target += 1

    x.rect.center = pg.math.Vector2.move_towards(
        pg.Vector2(x.rect.center), x.points[x.target], 5)
    x.set_state(x.animation[x.target])

    return x


class NPC(sprites.Sprite):
    def __init__(self, state, sheet, start, size, columns, points, animations):
        sprites.Sprite.__init__(self, state, sheet, start,
                                size, columns, pointToPoint)

        self.points = points
        self.animation = animations
        self.target = 0


def spawn():
    file = "Knight.png"
    start = [0, 0]
    size = [32, 32]
    frame_data = [13, 8, 10, 10, 10]
    points = [(500, 500), (500, 800), (800, 800)]
    animations = [States.IDLE, States.WALK, States.ATK]
    sprite = NPC(States.IDLE, file, start,
                 size, frame_data, points, animations)
    sprite.rect.center = (800, 800)
    sprite.flip = True
    sprite.scale_by(5)
    return sprite
