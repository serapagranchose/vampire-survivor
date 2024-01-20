import pygame
from globals import *


class Player :
    def __init__(self, entity):
        self.entity = entity
        self.color = ((255, 0, 0))


    def check_col(self, obstacle):
        if  ((
            self.entity.right <= obstacle.right and self.entity.right >= obstacle.left
             ) or (self.entity.left >= obstacle.left and self.entity.left <= obstacle.right
                   )) and ((self.entity.top >= obstacle.top and self.entity.top <= obstacle.bottom
                       ) or (self.entity.bottom <= obstacle.bottom and self.entity.bottom >= obstacle.top)): 
            return True

    