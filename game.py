import pygame as pg
import input
import sprites

fps = 60
SCREENRECT = pg.Rect(0, 0, 1920, 1080)


def movement(x, input):
    # Movement incrementers
    if input.is_pressed(pg.K_d):
        x.velocity[0] += 1
    if input.is_pressed(pg.K_a):
        x.velocity[0] -= 1
    if input.is_pressed(pg.K_s):
        x.velocity[1] += 1
    if input.is_pressed(pg.K_w):
        x.velocity[1] -= 1

    # Acceleration
    x.rect[0] += x.velocity[0]
    x.rect[1] += x.velocity[1]

    # Friction
    x.velocity[0] -= x.velocity[0] * 0.1
    x.velocity[1] -= x.velocity[1] * 0.1

    return x


class Game:
    def __init__(self):
        pg.init()
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
        self.player = sprites.Sprite("Knight.png", [0, 0], [
                                     32, 32], 13, 1, controller=movement)
        self.sprites = pg.sprite.RenderPlain(self.player)

        # Load background, this will be moved to Environment load function
        self.bg = pg.image.load("CS370_Room_Art.png")
        self.bg = pg.transform.scale(self.bg, (1920, 1080))

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

    def render(self):
        self.screen.fill("black")
        self.screen.blit(self.bg, (0, 0))
        self.sprites.draw(self.screen)
        pg.display.flip()

    def clean(self):
        pg.quit()
