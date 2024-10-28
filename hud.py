import pygame

class hud:

    currentSlot = None

    def collision(self,x,y,x2,y2,w):
        if x + w > x2 > x and y+w > y2 > y:
            return True
        else:
            return False

    class slotClass:
        def __init__(self,x,y):
            self.x = x
            self.y = y

        def draw(self, win, collision):
            if collision :pygame.draw.rect(win, (128, 0, 0), (self.x, self.y, 50, 50))
            else:pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))

    slotArray = []
    slotCount = 9

    while len(slotArray) != slotCount:
        slotArray.append(slotClass(100+len(slotArray)*70,50))

    def render(self, screen):
        mx,my = pygame.mouse.get_pos()
        for i in self.slotArray:
            i.draw(screen,self.collision(i.x, i.y, mx, my, 66))
        pygame.display.update()
