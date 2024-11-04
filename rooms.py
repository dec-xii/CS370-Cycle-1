# room.py
import pygame as pg
from player import controller

ACCEL = 3
class Room:
    def __init__(self, room_id, doors, items, backgrounds, collider_rect, spawn_positions):
        self.room_id = room_id
        self.doors = doors  # List of door objects with positions and destinations
        self.items = items  # List of items specific to the room
        self.background = backgrounds
        self.collider_rect = collider_rect
        self.spawn_positions = spawn_positions

    def draw(self, screen):
        # Draw all items and doors in the room
        # screen.fill((0, 0, 0))  # Clear the screen

        screen.fill("black")

        screen.blit(self.background, (0, 0))

        for door in self.doors:
            pg.draw.rect(screen, door.get("color", "blue"),
                         door["rect"])  # Draw doors as rectangles
        for item in self.items:
            # Draw other items as white rectangles
            pg.draw.rect(screen, "white", item)

    def check_collision(self, player_rect):
        # Check if the player collides with any door
        for door in self.doors:
            if player_rect.colliderect(door["rect"]):
                    
                # Change the door's color to green when collided
                door["color"] = "green"
                target_room = door["target_room"]
                
                 # Get the spawn position for the target room
                if target_room in self.spawn_positions:
                    spawn_position = self.spawn_positions[target_room]
                
                # Update player's position to the spawn position of the target room
                player_rect.topleft = spawn_position
        
                # Return the target room if collision happens
                return target_room
            else:
                door["color"] = "blue"  # Reset color if no collision
        
        # Check if player is outside room bounds
        if not self.collider_rect.contains(player_rect):
            if player_rect.left < self.collider_rect.left:
                player_rect.left = self.collider_rect.left
            if player_rect.right > self.collider_rect.right:
                player_rect.right = self.collider_rect.right
            if player_rect.top < self.collider_rect.top:
                player_rect.top = self.collider_rect.top
            if player_rect.bottom > self.collider_rect.bottom:
                player_rect.bottom = self.collider_rect.bottom
            print("Player is out of bounds!")
            
        return None

   


def load_rooms():
    # Define doors as rectangles with a destination room ID
    # Door to Room 2
    room1_doors = [{"rect": pg.Rect(
        830, 500, 250, 300), "target_room": 2}]

    bg1 = pg.image.load("CS370_Room_Art.png")
    bg1 = pg.transform.scale(bg1, (1920, 1080))

    bg2 = pg.image.load("CS370_Room_Art2.png")
    bg2 = pg.transform.scale(bg2, (1920, 1080))
    
    bg3 = pg.image.load("CafeArt.png")
    bg3 = pg.transform.scale(bg3, (1920, 1080))
    
    room1_collider = pg.Rect(100, 700, 1720, 300)
    room2_collider = pg.Rect(-100, 550, 1950, 500)
    room3_collider = pg.Rect(-100, 550, 1950, 500)
    
    room1_spawn_positions = {2: (800, 900)}
    room2_spawn_positions = {1: (830, 900), 3: (100, 700)}
    room3_spawn_positions = {2: (1850, 700)}

    # Door back to Room 1
    room2_doors = [{"rect": pg.Rect(
        830, 1000, 200, 50), "target_room": 1},
                   {"rect": pg.Rect(
        1850, 800, 200, 200), "target_room": 3}]
    
    room3_doors = [{"rect": pg.Rect(
        -100, 1000, 200, 200), "target_room": 2}]

    # Define room items
    room1_items = []  
    # A white square object in Room 2
    room2_items = [pg.Rect(400, 700, 50, 50)]
    room3_items = [pg.Rect(400, 700, 50, 50)]

    # Create the rooms
    room1 = Room(1, room1_doors, room1_items, bg1, room1_collider, room1_spawn_positions)
    room2 = Room(2, room2_doors, room2_items, bg2, room2_collider, room2_spawn_positions)
    room3 = Room(3, room3_doors, room3_items, bg3, room3_collider, room3_spawn_positions)
    

    # Return rooms as a dictionary
    return {1: room1, 2: room2, 3: room3}
