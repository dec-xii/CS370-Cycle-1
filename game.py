import pygame as pg
import input
import sprites

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

    x.rect[0] += x.velocity[0]
    x.rect[1] += x.velocity[1]

    return x



class Game:
    def __init__(self):
        self.running = False
        self.x, self.y = 500, 500  # Initial position of the circle
        self.speed = 5  # Speed of the circle's movement

    def start(self):
        self.running = True
        pg.init()
        self.input = input.Input()
        self.screen = pg.display.set_mode((1920, 1080))
        self.clock = pg.time.Clock()
<<<<<<< HEAD
=======
        self.deltaTime = 0

        self.player = sprites.Sprite("Knight.png", [0, 0], [
                                     32, 32], 13, 1, controller=movement)
        self.sprites = pg.sprite.RenderPlain(self.player)
>>>>>>> origin/Declan_Branch

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
        self.input.update()

    def update(self):
<<<<<<< HEAD
        keys = pg.key.get_pressed()  # Get the state of all keys
        if keys[pg.K_w]:  # Move up
            self.y -= self.speed
        if keys[pg.K_s]:  # Move down
            self.y += self.speed
        if keys[pg.K_a]:  # Move left
            self.x -= self.speed
        if keys[pg.K_d]:  # Move right
            self.x += self.speed

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear the screen (black background)
        pg.draw.circle(self.screen, "red", (self.x, self.y), 40)  # Draw the circle
=======
        self.player.update(self.deltaTime, self.input)
        self.deltaTime = self.clock.tick(fps) / 1000

    def render(self):
        self.screen.fill("black")
        self.sprites.draw(self.screen)
>>>>>>> origin/Declan_Branch
        pg.display.flip()

    def clean(self):
        pg.quit()
        
        

        

