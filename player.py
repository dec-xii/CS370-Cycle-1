import pygame as pg
import json
from enum import Enum
import sprites
import os
from constants import MAIN_PATH

ACCEL = 3
FRICTION = 0.7


class States(Enum):
    SIDE = 0
    FRONT = 1
    BACK = 2


def controller(x, input):
    match x.state:
        case x.state if x.state in [States.SIDE, States.FRONT, States.BACK]:
            state = States.FRONT
            # Movement incrementers
            if input.is_pressed(pg.K_d):
                x.velocity[0] += ACCEL
                state = States.SIDE
                x.flip = False
            if input.is_pressed(pg.K_a):
                x.velocity[0] -= ACCEL
                x.flip = True
                state = States.SIDE
            if input.is_pressed(pg.K_s):
                x.velocity[1] += ACCEL
                state = States.FRONT
                x.flip = False
            if input.is_pressed(pg.K_w):
                x.velocity[1] -= ACCEL
                state = States.BACK
                x.flip = False
            x.set_state(state)

    # Acceleration
    x.rect.center += x.velocity

    # Friction
    x.velocity *= FRICTION

    return x


def player():
    player_path = os.path.join(MAIN_PATH, "Entities/Player.json")
    with open(player_path) as f:
        data = json.load(f)
        print(player_path)
        sprite = sprites.Sprite(
            States.FRONT, data["file"], data["start"], data["size"], data["frame_data"], data["frame_rate"], controller)

    if "center" in data:
        sprite.rect.center = data["center"]
    if "scale" in data:
        sprite.scale_by(data["scale"])

    return sprite
