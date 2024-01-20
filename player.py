import pygame
from globals import *


class Player :
    def __init__(self, entity):
        self.entity = entity

    def move(self, key) :
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            self.entity.move_ip(0, 0 if self.entity.y - 1 <= 400 else -1 )
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            self.entity.move_ip(0, 0 if self.entity.y + 1 >= SCREEN_HEIGHT - PLAYER_HEIGHT else 1)
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            self.entity.move_ip(0 if self.entity.x - 1 <= 0 else -1, 0)
        if key[pygame.K_d] == True  or key[pygame.K_RIGHT] == True:
            self.entity.move_ip(0 if self.entity.x + 1 >= ZONE_WIDTH - PLAYER_WIDTH else 1, 0)

    def check_col(self, obstacle):
        if  ((
            self.entity.right <= obstacle.right and self.entity.right >= obstacle.left
             ) or (self.entity.left >= obstacle.left and self.entity.left <= obstacle.right
                   )) and ((self.entity.top >= obstacle.top and self.entity.top <= obstacle.bottom
                       ) or (self.entity.bottom <= obstacle.bottom and self.entity.bottom >= obstacle.top)): 
            return True

    