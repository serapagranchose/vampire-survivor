import pygame
from globals import *
from os import listdir
from os.path import isfile, join

def get_background(name):
    image = pygame.image.load(join("assets", "backgrounds", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(SCREEN_WIDTH // width + 1):
        for j in range(SCREEN_HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

class Background(pygame.sprite.Sprite) :
    def __init__(self, x, y):
        self.image = pygame.image.load(join("assets", "backgrounds", BACKGROUND_IMAGE))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = []
        self.buildTiles()
        self.x = x
        self.y = y

    def draw(self, win):
        for tile in self.tiles:
            win.blit(self.tile_image, tuple(map(lambda i, j: i - j, tile, (self.x, self.y))))
        
        pygame.display.update()

    def move(self, key):
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            self.y = self.y - 1
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            self.y = self.y + 1
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            self.x = self.x - 1
        if key[pygame.K_d] == True  or key[pygame.K_RIGHT] == True:
            self.x = self.x + 1

    def buildTiles(self) :
        self.tiles = []
        for i in range(SCREEN_WIDTH // self.width + 1):
            for j in range(SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width, j * self.height)
                self.tiles.append(pos)