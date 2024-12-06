import pygame
import sys
import game
import os
from constants import MAIN_PATH

pygame.mixer.init()

pygame.init()

# display
Width, Height = 1920, 1080
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Main Menu")

# colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

menu_state = "menu"
game_start = True


# button class

class Button:
    def __init__(self, text, x, y, width, height, press=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 40)
        self.color = red
        self.hover_color = green
        self.press = press

    def draw(self, place):
        # draw button
        pygame.draw.rect(place, self.color if not self.is_hovered()
                         else self.hover_color, self.rect)
        # render button text
        text_place = self.font.render(self.text, True, white)
        text_rect = text_place.get_rect(center=self.rect.center)
        place.blit(text_place, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def click(self):
        if self.is_hovered() and self.press:
            self.press()

# starting the game


def game_start(menu):
    pygame.mixer.music.stop()
    menu.running = False
    menu.start_game = True


def game_quit():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

# menu class


class Menu:
    def __init__(self):
        self.running = True
        self.start_game = False
        self.buttons = [
            Button("Start", 860, 450, 200, 50, lambda: game_start(self)),
            Button("Quit", 860, 550, 200, 50, game_quit)
        ]

        self.title_font = pygame.font.SysFont("Comic Sans", 200)
        self.title_text = "Escaperesque"

    def start(self):
        self.game = game.Game()
        pygame.mixer.music.load(os.path.join(
            MAIN_PATH, "Sounds/background_music.wav"))
        pygame.mixer.music.play(-1, 0.0)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    button.click()

    def update(self):

        if self.start_game:
            game_start(self)

    def render(self):
        background = pygame.image.load(os.path.join(
            MAIN_PATH, "Assets/images/CS370_Menu_Background.jpg"))
        background = pygame.transform.scale(background, (1920, 1080))
        screen.blit(background, (0, 0))
        # render title
        title_surface = self.title_font.render(self.title_text, True, blue)
        title_rect = title_surface.get_rect(center=(Width // 2, 200))
        screen.blit(title_surface, title_rect)

        for button in self.buttons:
            button.draw(screen)

            # update screen
        pygame.display.flip()

    def clean(self):
        pygame.quit()
