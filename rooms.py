# room.py
import pygame as pg

class Room:
    def __init__(self, room_id, doors, items):
        self.room_id = room_id
        self.doors = doors  # List of door objects with positions and destinations
        self.items = items  # List of items specific to the room

    def draw(self, screen):
        # Draw all items and doors in the room
        screen.fill((0, 0, 0))  # Clear the screen
        for door in self.doors:
            pg.draw.rect(screen, door.get("color", "blue"), door["rect"])  # Draw doors as rectangles
        for item in self.items:
            pg.draw.rect(screen, "white", item)  # Draw other items as white rectangles

    def check_collision(self, player_rect):
        # Check if the player collides with any door
        for door in self.doors:
            if player_rect.colliderect(door["rect"]):
                door["color"] = "green"  # Change the door's color to green when collided
                return door["target_room"]  # Return the target room if collision happens
            else:
                door["color"] = "blue"  # Reset color if no collision
        return None


def load_rooms():
    # Define doors as rectangles with a destination room ID
    room1_doors = [{"rect": pg.Rect(900, 500, 50, 100), "target_room": 2}]  # Door to Room 2
    room2_doors = [{"rect": pg.Rect(100, 500, 50, 100), "target_room": 1}]  # Door back to Room 1

    # Define room items
    room1_items = []  # Empty room for now
    room2_items = [pg.Rect(400, 400, 50, 50)]  # A white square object in Room 2

    # Create the rooms
    room1 = Room(1, room1_doors, room1_items)
    room2 = Room(2, room2_doors, room2_items)

    # Return rooms as a dictionary
    return {1: room1, 2: room2}
