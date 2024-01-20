import pygame
from globals import *
from button import *

class Settings():
    def __init__(self):
        self.up = pygame.K_w
        self.down = pygame.K_s
        self.left = pygame.K_a
        self.right = pygame.K_d

    def set_key_bind(self, key, changed):
        not_allowed = [self.up, self.down, self.left, self.right, pygame.K_ESCAPE, pygame.K_SPACE]

        if (key not in not_allowed):
            self.

    def menu(self, screen):
        run = True

        font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial
        text = font.render('Pause Menu',True,(255,255,255))
        textrect = text.get_rect()
        print (text.get_height())
        textrect.center = (SCREEN_WIDTH * 0.5, text.get_height() * 2)

        right_img = pygame.image.load("./assets/buttons/menu/square/regular/right.png").convert_alpha()
        right_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/right.png").convert_alpha()
        button_scale = (right_img.get_height() / SCREEN_HEIGHT) * 2

        button_space = right_img.get_height() * 0.75
        right_button_height = (SCREEN_HEIGHT / 3)
        right_button = Button(SCREEN_WIDTH * 0.5, right_button_height, right_img, right_img_colored, button_scale)
        right_button.selected = True

        left_img = pygame.image.load("./assets/buttons/menu/square/regular/left.png").convert_alpha()
        left_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/left.png").convert_alpha()
        button_scale = (left_img.get_height() / SCREEN_HEIGHT) * 2
        left_button_height = (SCREEN_HEIGHT / 3)
        left_button = Button(SCREEN_WIDTH * 0.5, left_button_height, left_img, left_img_colored, button_scale)

        up_img = pygame.image.load("./assets/buttons/menu/square/regular/up.png").convert_alpha()
        up_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/up.png").convert_alpha()
        button_scale = (up_img.get_height() / SCREEN_HEIGHT) * 2
        up_button_height = (SCREEN_HEIGHT / 3)
        up_button = Button(SCREEN_WIDTH * 0.5, up_button_height, up_img, up_img_colored, button_scale)

        down_img = pygame.image.load("./assets/buttons/menu/square/regular/down.png").convert_alpha()
        down_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/down.png").convert_alpha()
        button_scale = (down_img.get_height() / SCREEN_HEIGHT) * 2
        down_button_height = (SCREEN_HEIGHT / 3)
        down_button = Button(SCREEN_WIDTH * 0.5, down_button_height, down_img, down_img_colored, button_scale)

        buttons = [right_button, left_button, up_button, down_button]

        while run:
            for button in buttons:
                action = button.draw(screen)
                if (action and right_button.selected):
                    pass
                if (action and left_button.selected):
                    pass
                if (action and up_button):
                    pass
                if (action and down_button):
                    pass
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT :
                    run = False
            screen.blit(text, textrect)
            pygame.display.update()
