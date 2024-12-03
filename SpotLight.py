import pygame as pg
import random
import math

class SpotLight:

    def __init__(self, pos_x, pos_y, collider_rect, win):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = 125.0
        self.speed = [10.0,10.0]
        self.direction = random.randint(0,360)
        self.crackEnergy = 1000
        self.crackCharge = 0
        self.collider_rect = collider_rect

    def collision_check(self, player_rect):
        if(pg.Rect(self.pos_x, self.pos_y, self.radius, self.radius).colliderect(player_rect)):
            return True
        return False

    def move(self):
        self.pos_x += self.speed[0] * math.cos(self.direction)
        self.pos_y += self.speed[1] * math.sin(self.direction)

    def render(self, win):
        self.move()

        if self.pos_x <= 0 or self.pos_x >= self.collider_rect.right:
            self.speed[0] = -self.speed[0]
        if self.pos_y <= 0 or self.pos_y >= self.collider_rect.bottom:
            self.speed[1] = -self.speed[1]

        pg.draw.circle(win, (255,255,0), (self.pos_x, self.pos_y), self.radius)
