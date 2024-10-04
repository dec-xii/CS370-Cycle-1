import pygame as pg
from enum import Enum
import sprites

ACCEL = 3
FRICTION = 0.7


# functional syntax
States = Enum('States', ['idle', 'walk', 'attack_1', 'attack_2', 'attack_3'])


def controller(x, input):
    state = 0
    x.flip = False

    # Movement incrementers
    if input.is_pressed(pg.K_d):
        x.velocity[0] += ACCEL
        state = 1
    if input.is_pressed(pg.K_a):
        x.velocity[0] -= ACCEL
        x.flip = True
        state = 1
    if input.is_pressed(pg.K_s):
        x.velocity[1] += ACCEL
        state = 1
    if input.is_pressed(pg.K_w):
        x.velocity[1] -= ACCEL
        state = 1
    if input.is_pressed(pg.K_x):
        state = 2

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
    return sprites.Sprite(file, start, size, frame_data, controller)
