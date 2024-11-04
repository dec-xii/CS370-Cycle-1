import pygame as pg
from enum import Enum
import sprites

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
    file = "CS370 Art-Sheet.png"
    start = [0, 0]
    size = [23, 48]
    frame_data = [3, 2, 2]
    sprite = sprites.Sprite(States.FRONT, file, start,
                            size, frame_data, controller)
    sprite.rect.center = (700, 700)
    sprite.scale_by(2)
    return sprite
