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



class Room:
    def __init__(self, room_id, doors, items):
        self.room_id = room_id
        self.doors = doors # List of door objects with positions and destinations
        self.items = items # List of items specific to the room
        
    def draw(self, screen):
        # Draw all items and doors in the room
        screen.fill((0,0,0)) # Clear the screen
        for door in self.doors:
            pg.draw.rect(screen,door.get("color", "blue"), door["rect"]) # Draw doors as blue rectangles
        for item in self.items:
            pg.draw.rect(screen, "white", item) # Draw other items as white rectangles
            
    def check_collision(self, player_rect):
    # Check if the player collides with any door
        for door in self.doors:
            if player_rect.colliderect(door["rect"]):
                door["color"] = "green"  # Change the color to green when collided
                return door["target_room"]  # Return the target room if collision happens
            else:
                door["color"] = "blue"  # Set it back to blue if no collision
        return None



class Game:
    def __init__(self):
        self.running = False
        #self.x, self.y = 500, 500  # Initial position of the circle
        self.speed = 5  # Speed of the circle's movement

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
        
        # Define doors as rectangles with a destination room ID
        room1_doors = [{"rect": pg.Rect(1800, 500, 50, 100), "target_room": 2}]  # Door to Room 2
        room2_doors = [{"rect": pg.Rect(100, 500, 50, 100), "target_room": 1}]  # Door back to Room 1
        
        # Define room items 
        room1_items = []  # Empty room for now
        room2_items = [pg.Rect(400, 400, 50, 50)]  # A white square object in Room 2
        
        # Create the rooms
        room1 = Room(1, room1_doors, room1_items)
        room2 = Room(2, room2_doors, room2_items)
        
        # Store the rooms in a dictionary
        self.rooms = {1: room1, 2: room2}

        self.current_room = self.rooms[1]  # Start in Room 1

    def event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
        self.input.update()

    def update(self):
        self.player.update(self.deltaTime, self.input)
        self.deltaTime = self.clock.tick(fps) / 1000
        
        player_rect = self.player.rect
        
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
        
        
        

        
        
        

        

