import pygame as pg
import os
import json
from enum import Enum
import sprites
import dialog
from constants import MAIN_PATH


class States(Enum):
    IDLE = 0
    WALK = 1
    ATK = 2


def pointToPoint(x, input):
    halt = False
    # Update the target
    if pg.Vector2(x.rect.center).distance_to(pg.Vector2(x.points[x.target])) < 10:
        if x.target == len(x.points) - 1:
            x.set_state(States.IDLE)
            halt = True
        else:
            x.target += 1

    if not halt:
        # Move towards the current target
        x.rect.center = pg.math.Vector2.move_towards(
            pg.Vector2(x.rect.center), x.points[x.target], 5)
        x.set_state(x.animation[x.target])

    return x


# The action performed once the player interacts with an NPC
def action(self):
    self.dialog.update()


class NPC(sprites.Sprite):
    def __init__(self, state, sheet, start, size, columns, points, frame_rate, animations, action):
        sprites.Sprite.__init__(self, state, sheet, start,
                                size, columns, frame_rate, pointToPoint)

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
    animations = [States.WALK, States.WALK]

    entities_path = os.path.join(MAIN_PATH, "Entities")

    # Iterate over the NPC files and laod each into a sprite
    for file in os.listdir(entities_path):
        if file != "Player.json":
            with open(os.path.join(entities_path, file)) as f:
                data = json.load(f)
                sprite = NPC(
                    States.IDLE, os.path.join(
                        MAIN_PATH, data["file"]), data["start"], data["size"],
                    data["frame_data"], data["points"], data["frame_rate"], animations, action)

    #  Set the starting location
    if "center" in data:
        sprite.rect.center = data["center"]

    # Set the srpite size
    if "scale" in data:
        sprite.scale_by(data["scale"])

    # Load the sprite's dialog
    sprite.dialog = dialog.Dialog()

    return sprite
