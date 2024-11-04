import pygame 
import sys
import game

pygame.init()

# display
Width, Height = 1920, 1080
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Main Menu")

# colors
blue = (0, 0, 255)
red = (255, 0 , 0)
black = (0, 0, 0,)


# button class
class Button:
    def __init__(self, text, x, y, width, height, press = None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 40)
        self.color = red
        self.hover_color = (0, 255, 0)
        self.press = press

    def draw(self, place):
        pygame.draw.rect(place, self.color if not self.is_hovered 
                         else self.hover_color, self.rect)
        text_place = self.font.render(self.text, True, blue)
        text_rect = text_place.get_rect(center = self.rect.center)
        place.blit(text_place, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def click(self):
        if self.is_hovered() and self.press:
            self.press()

# starting 
def game_start():
        global current_state
        current_state = game()

def game_quit():
        pygame.quit()
        sys.exit()



# menu class

class Menu:
    def start(self):
        self.game = game()

    def __init__(self):
        self.current_state = Menu
        self.buttons = [
    Button("Start", 200, 150, 200, 50, ( game_start(self))),
    Button("Options", 200, 220, 200, 50),
    Button("Quit", 200, 290, 200, 50, game_quit),]
        

    def run(self):
        while self.current_state == Menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.buttons:
                        button.click()

       
        

        # draw buttons
        for button in self.buttons:
            button.draw(screen)

        # update display
        pygame.display.flip()


    

        
    
        


    
    





  


        