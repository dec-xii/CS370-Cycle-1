import pygame

from player import States

class Tests:

    def run_animation_test(player):
        # Check the current state and position of the player
        if player.state == States.WALK:
            print("Debug: Walking")
        else:
            print("Debug: Idle")

        # Print the player's position
        #print(f"Debug: Player Position: {player.rect.topleft}") 