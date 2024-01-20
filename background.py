import pygame
from os.path import join

from globals import *



class Background :
    def __init__(self) :
        self.image = pygame.image.load(join("assets", "backgrounds", BACKGROUND_IMAGE))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = []
        self.buildTiles((0,0))


    def buildTiles(self, offset) :
        self.tiles = []
        for i in range(SCREEN_WIDTH // self.width + 1):
            for j in range(SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width - offset[0], j * self.height- offset[1])
                self.tiles.append(pos)

    