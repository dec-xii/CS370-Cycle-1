import pygame as pg
from enum import Enum
import sprites

ACCEL = 3
FRICTION = 0.7


# functional syntax
# States = Enum('States', ['IDLE', 'WALK', 'ATTACK_1', 'ATTACK_2', 'ATTACK_3'])

class States(Enum):
    IDLE = 0
    WALK = 1
    ATK1 = 2
    ATK2 = 3
    ATK3 = 4


def controller(x, input):
    match x.state:
        case States.ATK1:
            if x.complete:
                x.set_state(States.IDLE)
        case x.state if x.state in [States.IDLE, States.WALK]:
            state = States.IDLE
            # Movement incrementers
            if input.is_pressed(pg.K_d):
                x.velocity[0] += ACCEL
                state = States.WALK
                x.flip = False
            if input.is_pressed(pg.K_a):
                x.velocity[0] -= ACCEL
                x.flip = True
                state = States.WALK
            if input.is_pressed(pg.K_s):
                x.velocity[1] += ACCEL
                state = States.WALK
            if input.is_pressed(pg.K_w):
                x.velocity[1] -= ACCEL
                state = States.WALK
            if input.is_pressed(pg.K_x):
                state = States.ATK1
            x.set_state(state)

    # Acceleration
    x.rect.center += x.velocity

    # Friction
    x.velocity *= FRICTION

    return x


def player():
    file = "Knight.png"
    start = [0, 0]
    size = [32, 32]
    frame_data = [13, 8, 10, 10, 10]
    return sprites.Sprite(States.IDLE, file, start, size, frame_data, controller)
