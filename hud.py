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

        def draw(self, win, item_img, collision):
            if(item_img is not None):
                if collision:
                    colord_image = item_img.copy()
                    colord_image.fill("red", special_flags=pygame.BLEND_RGBA_MIN)
                    win.blit(colord_image, (self.x, self.y))
                else:
                    win.blit(item_img, (self.x, self.y))
            else:
                if collision:pygame.draw.rect(win, (128, 0, 0), (self.x, self.y, 50, 50))
                else:pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))

    slotArray = []
    slotCount = 9

    while len(slotArray) != slotCount:
        slotArray.append(slotClass(100+len(slotArray)*70,50))

    def render(self, screen, inventoryList):
        mx,my = pygame.mouse.get_pos()
        for i in range(self.slotCount):
            slot = self.slotArray[i]
            if (len(inventoryList) > i):
                slot.draw(screen,inventoryList[i].image,self.collision(slot.x, slot.y, mx, my, 66))
            else:
                slot.draw(screen,None,self.collision(slot.x, slot.y, mx, my, 66))
        pygame.display.update()
