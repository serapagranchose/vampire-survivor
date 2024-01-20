from random import *
import pygame
from globals import *


class Obstacle: 
    def __init__(self) :
        self.height = randint(10, 100)
        self.weight = randint(10, 100)
        self.color = COLORS[randint(0, 3)] 
        self.entity = pygame.Rect((randint(0, SCREEN_WIDTH), 0, self.height, self.weight))
        self.speed = randint(1, MAX_SPEED)

    def update(self) :
        self.entity.move_ip(0, self.speed)
