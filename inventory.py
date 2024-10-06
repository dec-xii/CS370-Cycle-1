
import pygame
pygame.init()
win = pygame.display.set_mode((800,600))


currentSlot = None


def collision(x,y,x2,y2,w):
    if x + w > x2 > x and y+w > y2 > y:
        return True
    else:
        return False


class slotClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, win):
        
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))

        
        if collision(self.x, self.y, mx, my, 66):
            global currentSlot
            pygame.draw.rect(win, (128, 0, 0), (self.x, self.y, 50, 50))

            
            currentSlot = slotArray.index(self)

        
        else:
            currentSlot = None


slotArray = []

slotCount = 9


#
while len(slotArray) != slotCount:
    slotArray.append(slotClass(100+len(slotArray)*70,50))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    mx,my = pygame.mouse.get_pos()
    win.fill((0,0,0))


    
    currentSlot = None
    for i in slotArray:
        i.draw(win)
        if currentSlot is not None:
            break

    print(currentSlot)

    pygame.display.update()
pygame.quit()