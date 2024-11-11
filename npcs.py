import pygame as pg
import os
import json
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


# The action performed once the player interacts with an NPC
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

    # Handles NPC-Player interactions
    def interact(self, player, input):
        self.dialog.visable = False
        # Detect the players's distance from the NPC
        if pg.Vector2(player.rect.center).distance_to(pg.Vector2(self.rect.center)) < self.radius:
            self.image.fill("yellow", special_flags=pg.BLEND_RGBA_MIN)
            self.dialog.visable = True
            if input.mouseUp(0) and self.rect.collidepoint(input.mouse_pos):
                self.action(self)

    def displayText(self, screen):
        self.dialog.display(self.rect.move(-10, 0), screen)


def spawn():
    # Load the anima     for each point
    animations = [States.IDLE]

    # Iterate over the NPC files and laod each into a sprite
    for file in os.listdir("Entities"):
        if file != "Player.json":
            with open("Entities/" + file) as f:
                data = json.load(f)
                sprite = NPC(
                    States.IDLE, data["file"], data["start"], data["size"],
                    data["frame_data"], data["points"], animations, action)

    #  Set the starting location
    if "center" in data:
        sprite.rect.center = data["center"]

    # Set the srpite size
    if "scale" in data:
        sprite.scale_by(data["scale"])

    # Load the sprite's dialog
    sprite.dialog = dialog.Dialog()

    return sprite
