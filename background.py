import pygame
from globals import *
from os import listdir
from os.path import isfile, join
import math

class Background(pygame.sprite.Sprite) :
    def __init__(self, x, y):
        self.image = pygame.image.load(join("assets", "backgrounds", BACKGROUND_IMAGE))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = self.buildTiles()
        self.x = x
        self.y = y

    def draw(self, win):
        for tile in self.tiles:
            #win.blit(self.image, tile)
            win.blit(self.image, tuple(map(lambda i, j: i - j, tile, (self.x, self.y))))
        
    def move(self, key):
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            self.y -= 1
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            self.y += 1
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            self.x -= 1
        if key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
            self.x += 1
        self.manage_tiles()

    def buildTiles(self) :
        self.tiles = []
        for i in range(-1, SCREEN_WIDTH // self.width + 1):
            for j in range(-1, SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width, j * self.height)
                self.tiles.append(pos)

        return self.tiles
    
    def manage_tiles(self):
        new_tiles = []
    
        for i in range(-1, SCREEN_WIDTH // self.width + 1):
            for j in range(-1, SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width + self.x, j * self.height + self.y)
                new_tiles.append(pos)

        self.tiles = new_tiles