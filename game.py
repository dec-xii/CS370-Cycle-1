import pygame as pg
import input
import player
from player import States
from rooms import load_rooms
from animation_tests import Tests

fps = 60
SCREENRECT = pg.Rect(0, 0, 1920, 1080)


class Game:
    def __init__(self):
        pg.init()
        self.x, self.y = 500, 500  # Initial position of the player
        self.speed = 5  # Player movement speed
        self.running = False
        self.input = input.Input()
        self.screen = pg.display.set_mode((1920, 1080))
        self.fullscreen = False
        self.clock = pg.time.Clock()
        self.deltaTime = 0
        self.winstyle = 0  # |FULLSCREEN
        self.bestdepth = pg.display.mode_ok(SCREENRECT.size, self.winstyle, 32)

    # Initialize

    def start(self):
        self.running = True
        self.player = player.player()
        self.sprites = pg.sprite.RenderPlain(self.player)

        # Load background, this will be moved to Environment load function
        self.bg = pg.image.load("CS370_Room_Art.png")
        self.bg = pg.transform.scale(self.bg, (1920, 1080))

        # Load rooms using the load_rooms function
        self.rooms = load_rooms()
        self.current_room = self.rooms[1]  # Start in Room 1

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.running = False
                # Code for changing to fullscreen adapted from:
                # https://github.com/pygame/pygame/blob/main/examples/aliens.py
                if e.key == pg.K_f:
                    if not self.fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = self.screen.copy()
                        self.screen = pg.display.set_mode(
                            SCREENRECT.size, self.winstyle |
                            pg.FULLSCREEN, self.bestdepth
                        )
                        self.screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = self.screen.copy()
                        self.screen = pg.display.set_mode(
                            SCREENRECT.size, self.winstyle, self.bestdepth
                        )
                        self.screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    self.fullscreen = not self.fullscreen
        self.input.update()

    def update(self):
        self.player.update(self.deltaTime, self.input)
        self.deltaTime = self.clock.tick(fps) / 1000

        # Player's hitbox for collision detection
        player_rect = self.player.rect.copy()  # Get the player's rectangle
        # Ensure the rect reflects the player's position
        player_rect.topleft = (self.player.rect.x, self.player.rect.y)

        # Check for collision with a door in the current room
        next_room = self.current_room.check_collision(self.player.rect)
        if next_room:
            self.current_room = self.rooms[next_room]  # Switch to the new room

        # Call the animation test function
        Tests.run_animation_test(self.player)

    def render(self):
        self.current_room.draw(self.screen)
        self.sprites.draw(self.screen)
        pg.display.flip()

    def clean(self):
        pg.quit()
