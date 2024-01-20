import pygame
from globals import *

class Player(pygame.sprite.Sprite) :
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height, entity, sheet, load_sprite_sheets, flip):
        self.rect = pygame.Rect(x, y, width, height)
        self.entity = entity
        self.sheet = sheet
        self.direction = "left"
        self.animation_count = 0
        self.load_sprite_sheets = load_sprite_sheets
        self.flip = flip

    def draw(self, win):
        # self.sprite = self.load_sprite_sheets("characters", "MiniNobleMan", 32, 32, True)["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))

    def move(self, key):
        sprite_sheet = "idle"
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            sprite_sheet = "run"
            self.entity.move_ip(0, 0 if self.entity.y - 1 <= 400 else -1 )
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            sprite_sheet = "run"
            self.entity.move_ip(0, 0 if self.entity.y + 1 >= SCREEN_HEIGHT - PLAYER_HEIGHT else 1)
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            sprite_sheet = "run"
            self.entity.move_ip(0 if self.entity.x - 1 <= 0 else -1, 0)
            if self.direction != 'left':
                self.direction = 'left'
                self.animation_count = 0
        if key[pygame.K_d] == True  or key[pygame.K_RIGHT] == True:
            sprite_sheet = "run"
            self.entity.move_ip(0 if self.entity.x + 1 >= ZONE_WIDTH - PLAYER_WIDTH else 1, 0)
            if self.direction != 'right':
                self.direction = 'right'
                self.animation_count = 0

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.load_sprite_sheets("characters", "MiniNobleMan", 32, 32, True)[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY % len(sprites))
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

        self.color = ((255, 0, 0))


    def check_col(self, obstacle):
        if  ((
            self.entity.right <= obstacle.right and self.entity.right >= obstacle.left
             ) or (self.entity.left >= obstacle.left and self.entity.left <= obstacle.right
                   )) and ((self.entity.top >= obstacle.top and self.entity.top <= obstacle.bottom
                       ) or (self.entity.bottom <= obstacle.bottom and self.entity.bottom >= obstacle.top)): 
            return True

    