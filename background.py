import pygame
from os.path import join

from globals import *



class Background :
    def __init__(self) :
        self.image = pygame.image.load(join("assets", "backgrounds", BACKGROUND_IMAGE))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = []
        self.buildTiles()


    def buildTiles(self) :
        self.tiles = []
        for i in range(SCREEN_WIDTH // self.width + 1):
            for j in range(SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width, j * self.height)
                self.tiles.append(pos)

    