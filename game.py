import pygame as pg
import input
import sprites
from rooms import load_rooms 

fps = 60

def movement(x, input):
    if input.is_pressed(pg.K_d):
        x.velocity[0] += 1
    if input.is_pressed(pg.K_a):
        x.velocity[0] -= 1
    if input.is_pressed(pg.K_s):
        x.velocity[1] += 1
    if input.is_pressed(pg.K_w):
        x.velocity[1] -= 1

    # Update the position using pg.Rect (x.rect is a pg.Rect now)
    x.rect.x += x.velocity[0]
    x.rect.y += x.velocity[1]

    return x

class Game:
    def __init__(self):
        self.running = False
        self.x, self.y = 500, 500  # Initial position of the player
        self.speed = 5  # Player movement speed

    def start(self):
        self.running = True
        pg.init()
        self.input = input.Input()
        self.screen = pg.display.set_mode((1920, 1080))
        self.clock = pg.time.Clock()
        self.deltaTime = 0

        self.player = sprites.Sprite("Knight.png", [0, 0], [
                                     32, 32], 13, 1, controller=movement)
        self.sprites = pg.sprite.RenderPlain(self.player)

        # Load rooms using the load_rooms function
        self.rooms = load_rooms()

        self.current_room = self.rooms[1]  # Start in Room 1

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
        self.input.update()

    def update(self):
        self.player.update(self.deltaTime, self.input)
        self.deltaTime = self.clock.tick(fps) / 1000

        # Player's hitbox for collision detection
        player_rect = self.player.rect.copy()  # Get the player's rectangle
        player_rect.topleft = (self.player.rect.x, self.player.rect.y)  # Ensure the rect reflects the player's position

        # Check for collision with a door in the current room
        next_room = self.current_room.check_collision(player_rect)
        if next_room:
            self.current_room = self.rooms[next_room]  # Switch to the new room

    def render(self):
        self.screen.fill("black")
        self.current_room.draw(self.screen)
        self.sprites.draw(self.screen)
        pg.display.flip()

    def clean(self):
        pg.quit()


