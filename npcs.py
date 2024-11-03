import pygame as pg
from enum import Enum
import sprites
import dialog


class States(Enum):
    IDLE = 0
    WALK = 1
    ATK = 2


def pointToPoint(x, input):
    # Update the target
    if x.rect.center == x.points[x.target]:
        if x.target == len(x.points) - 1:
            x.target = 0
        else:
            x.target += 1

    # Move towards the current target
    x.rect.center = pg.math.Vector2.move_towards(
        pg.Vector2(x.rect.center), x.points[x.target], 5)
    x.set_state(x.animation[x.target])

    return x


def action(self):
    self.dialog.update()


class NPC(sprites.Sprite):
    def __init__(self, state, sheet, start, size, columns, points, animations, action):
        sprites.Sprite.__init__(self, state, sheet, start,
                                size, columns, pointToPoint)

        self.points = points
        self.action = action
        self.animation = animations
        self.target = 0
        self.radius = 100

        self.dialog = None

    def update(self, deltaTime, input):
        # Update the sprite location
        if self.controller:
            self = self.controller(self, input)
        if self.animated:
            self.next_frame(deltaTime)

    def interact(self, player, input):
        if pg.Vector2(player.rect.center).distance_to(pg.Vector2(self.rect.center)) < self.radius:
            self.image.fill("yellow", special_flags=pg.BLEND_RGBA_MIN)
            self.dialog.visable = True
            if input.mouseUp(0) and self.rect.collidepoint(input.mouse_pos):
                self.action(self)
        else:
            self.dialog.visable = False

    def displayText(self, screen):
        self.dialog.display(self.rect.move(-10, 0), screen)


def spawn():
    file = "Knight.png"
    start = [0, 0]
    size = [32, 32]
    frame_data = [13, 8, 10, 10, 10]
    points = [(800, 800)]
    animations = [States.IDLE]
    sprite = NPC(States.IDLE, file, start,
                 size, frame_data, points, animations, action)
    sprite.rect.center = (800, 800)
    sprite.flip = True
    sprite.scale_by(5)
    sprite.dialog = dialog.Dialog()

    return sprite
