import pygame as pg
import sprites


def controller(x, input):
    state = "idle"

    # Movement incrementers
    if input.is_pressed(pg.K_d):
        x.velocity[0] += 1
        state = "walk"
    if input.is_pressed(pg.K_a):
        x.velocity[0] -= 1
        state = "walk"
    if input.is_pressed(pg.K_s):
        x.velocity[1] += 1
        state = "walk"
    if input.is_pressed(pg.K_w):
        x.velocity[1] -= 1
        state = "walk"

    x.set_state(state)

    # Acceleration
    x.rect[0] += x.velocity[0]
    x.rect[1] += x.velocity[1]

    # Friction
    x.velocity[0] -= x.velocity[0] * 0.1
    x.velocity[1] -= x.velocity[1] * 0.1

    return x


def player():
    return sprites.Sprite("Knight.png", [0, 0], [32, 32], [13, 8], [
        "idle", "walk"], 2, controller)
