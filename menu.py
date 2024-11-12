import pygame
import sys
import game  # Import the game to start it


pygame.init()

# display
Width, Height = 1920, 1080
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Main Menu")

# colors
blue = (0, 0, 255)
green = (0, 255, 0)  
red = (255, 0 , 0)
white = (255, 255, 255)  
black = (0,0,0)

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
        # Draw the button rectangle with the appropriate color
        pygame.draw.rect(place, self.color if not self.is_hovered()
                         else self.hover_color, self.rect)
        # Render the text on the button
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
    menu.running = False  # Stop the menu loop
    menu.start_game = True  # Flag to start the game

def game_quit():
    pygame.quit()
    sys.exit()

# menu class
class Menu:
    def __init__(self):
        self.running = True  
        self.start_game = False  
        self.buttons = [
            Button("Start", 200, 150, 200, 50, lambda: game_start(self)),
            Button("Quit", 200, 220, 200, 50, game_quit)
        ]

    def start(self):
        self.game = game.Game()  

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
        screen.fill(black)  
        for button in self.buttons:
            button.draw(screen)
            
            #update screen
        pygame.display.flip()  

    def clean(self):
        pygame.quit()

