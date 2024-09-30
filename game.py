import pygame as pg



class Game:
    def __init__(self):
        self.running = False
        self.x, self.y = 500, 500  # Initial position of the circle
        self.speed = 5  # Speed of the circle's movement

    def start(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((1920, 1080))
        self.clock = pg.time.Clock()

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def update(self):
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
        pg.display.flip()

    def clean(self):
        pg.quit()
        
        

        

