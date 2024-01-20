import pygame

class Button():
    def __init__(self, x, y, image, image_colored, scale):
        width = image.get_width()
        height = image.get_height()
        self.img = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.colored_img = pygame.transform.scale(image_colored, (int(width * scale), (int(height * scale))))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.selected = False

    def draw(self, surface):
        action = False

        img = self.img

        if (self.selected):
            img = self.colored_img
            for event in pygame.event.get() :
                if(event.type==pygame.KEYDOWN):
                    if (event.key==pygame.K_RETURN):
                        self.clicked = True
                        action = True

        else:
            img = self.img
        
        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False

        surface.blit(img, (self.rect.x, self.rect.y))

        return action