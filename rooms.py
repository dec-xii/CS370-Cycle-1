# room.py
import pygame as pg
import npcs
from player import controller
from dq_object import dq_item, items
import SpotLight as sl

pg.mixer.init()
DOOR_OPENING = pg.mixer.Sound("Sounds/door-opening.wav")

ACCEL = 3


class Room:
    def __init__(self, room_id, doors, items, backgrounds, collider_rect, spawn_positions, inventory, entites=[], spotLights=[]):
        self.room_id = room_id
        self.doors = doors  # List of door objects with positions and destinations
        self.items = items  # List of items specific to the room
        self.background = backgrounds
        self.collider_rect = collider_rect
        self.spawn_positions = spawn_positions
        self.entites = entites
        self.inventory = inventory
        self.spotLights = spotLights

    def draw(self, screen):
        # Draw all items and doors in the room
        # screen.fill((0, 0, 0))  # Clea the screen

        screen.fill("black")

        screen.blit(self.background, (0, 0))

        for door in self.doors:
            pg.draw.rect(screen, door.get("color", "blue"),
                         door["rect"])  # Draw doors as rectangles
        for item in self.items:
            # Draw other items as white rectangles
            item.render(screen)

        pg.sprite.RenderPlain(self.entites).draw(screen)
        for npc in self.entites:
            npc.displayText(screen)

        # Render spotlights
        for spot in self.spotLights:
            spot.render(screen)

    def check_collision(self, player_rect):
        # Check if the player collides with any door
        for door in self.doors:
            if player_rect.colliderect(door["rect"]):
                target_room = door["target_room"]
                if (target_room == 4):
                    # Check if key
                    keyFound = False
                    for item in self.inventory.get_item_list():
                        if (item.name == "keys"):
                            print("Key Found")
                            keyFound = True
                            self.inventory.get_item_list().remove(item)
                    if (not keyFound):
                        door["color"] = "red"
                    else:
                        spawn = (1850, 700)
                        if target_room in self.spawn_positions:
                            spawn = self.spawn_positions[target_room]

                        # Update player's position to the spawn position of the target room
                        player_rect.topleft = spawn

                        # Return the target room if collision happens
                        return target_room
                else:
                    # Change the door's color to green when collided
                    door["color"] = "green"
                    print("target room ", target_room)
                    # Get the spawn position for the target room
                    spawn = (1850, 700)
                    if target_room in self.spawn_positions:
                        spawn = self.spawn_positions[target_room]
                        DOOR_OPENING.play()

                    # Update player's position to the spawn position of the target room
                    player_rect.topleft = spawn

                    # Return the target room if collision happens
                    return target_room
            else:
                door["color"] = "blue"  # Reset color if no collision

        # Check item collision
        for item in self.items:
            if (item.check_collision(player_rect)):
                # add to inventory
                self.inventory.add_item(item)
                # delete item
                self.items.remove(item)

        # Check spotlight collision
        for spot in self.spotLights:
            if (spot.collision_check(player_rect)):
                # Game Over
                target_room = 5
                spawn = (1850, 700)
                player_rect.topleft = spawn
                return target_room

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

        return None


def load_rooms(obj_map, inv):
    # Define doors as rectangles with a destination room ID
    # Door to Room 2
    room1_doors = [{"rect": pg.Rect(
        830, 500, 250, 300), "target_room": 2}]

    bg1 = pg.image.load(r'Assets/Rooms/CS370_Room_Art.png')
    bg1 = pg.transform.scale(bg1, (1920, 1080))

    bg2 = pg.image.load(r'Assets/Rooms/CS370_Room_Art2.png')
    bg2 = pg.transform.scale(bg2, (1920, 1080))

    bg3 = pg.image.load(r'Assets/Rooms/CafeArt.png')
    bg3 = pg.transform.scale(bg3, (1920, 1080))

    bg4 = pg.image.load(r'Assets/objects/gameover.png')
    bg4 = pg.transform.scale(bg4, (1920, 1080))

    bg5 = pg.image.load(r'Assets/objects/died.png')
    bg5 = pg.transform.scale(bg5, (1920, 1080))

    room1_collider = pg.Rect(100, 700, 1720, 300)
    room2_collider = pg.Rect(-100, 550, 1950, 500)
    room3_collider = pg.Rect(-100, 550, 1950, 500)
    room4_collider = pg.Rect(-100, 550, 1950, 500)
    room5_collider = pg.Rect(-100, 550, 1950, 500)

    room1_spawn_positions = {2: (800, 900)}
    room2_spawn_positions = {1: (830, 900), 3: (100, 700)}
    room3_spawn_positions = {2: (1850, 700)}
    room4_spawn_positions = {3: (1850, 700), 4: (1850, 700)}
    room5_spawn_positions = {}

    # Door back to Room 1
    room2_doors = [{"rect": pg.Rect(
        830, 1000, 200, 50), "target_room": 1},
        {"rect": pg.Rect(
            1850, 800, 200, 200), "target_room": 3}]

    room3_doors = [{"rect": pg.Rect(
        -100, 1000, 200, 200), "target_room": 2},
        {"rect": pg.Rect(
            1850, 800, 200, 200), "target_room": 4}]
    room4_doors = []
    room5_doors = []

    # Define room items
    room1_items = []
    # A white square object in Room 2
    room2_items = [dq_item(obj_map[items.CIGARETTE.value], 1200, 900),
                   dq_item(obj_map[items.KEYS.value], 600, 800),
                   dq_item(obj_map[items.LIGHTER.value], 500, 900),
                   dq_item(obj_map[items.POSTER.value], 200, 400),
                   dq_item(obj_map[items.UTENSILS.value], 1500, 1000),
                   dq_item(obj_map[items.BED_SHEETS.value], 100, 900)]
    room3_items = []
    room4_items = []
    room5_items = []

    room1_sLights = []
    room2_sLights = [sl.SpotLight(1100, 700, room1_collider, bg2)]
    room3_sLights = [sl.SpotLight(900, 900, room1_collider, bg3), sl.SpotLight(
        900, 750, room1_collider, bg3)]
    room4_sLights = []
    room5_sLights = []

    # Create the rooms
    room1 = Room(1, room1_doors, room1_items, bg1, room1_collider,
                 room1_spawn_positions, inv, [npcs.spawn()], room1_sLights)
    room2 = Room(2, room2_doors, room2_items, bg2, room2_collider,
                 room2_spawn_positions, inv, [], room2_sLights)
    room3 = Room(3, room3_doors, room3_items, bg3, room3_collider,
                 room3_spawn_positions, inv, [npcs.spawn()], room3_sLights)
    room4 = Room(4, room4_doors, room4_items, bg4, room4_collider,
                 room4_spawn_positions, inv, [], room4_sLights)
    room5 = Room(5, room5_doors, room5_items, bg5, room5_collider,
                 room5_spawn_positions, inv, [], room5_sLights)

    # Return rooms as a dictionary
    return {1: room1, 2: room2, 3: room3, 4: room4, 5: room5}
