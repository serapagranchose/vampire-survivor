from random import *
import pygame
from globals import *


class Obstacle: 
    def __init__(self, offset=(0,0)) :
        self.height = randint(10, 100)
        self.weight = randint(10, 100)
        self.x , self.y = START_POS[randint(0, 3)]
        self.x -= offset[0]
        self.y -= offset[1]
        self.entity = pygame.Rect((self.x, self.y , self.height, self.weight))
        self.speed = randint(0, MAX_SPEED)
        self.hp = 100

    def getDirection(self, offset) :
        if (self.x < offset[0]) :
            self.x += self.speed * 0.1
        if (self.x > offset[0]) :
            self.x -= self.speed
        if (self.y < offset[1]) :
            self.y += self.speed
        if (self.y > offset[1]) :
            self.y -= self.speed

    def updatePos(self, offset) :
        print(f'offset => {offset}')
        self.getDirection([SCREEN_WIDTH/2 - offset[0] , SCREEN_HEIGHT/2 - offset[1]])
        x = self.x + offset[0]
        y = self.y + offset[1]
        self.entity.x = x
        self.entity.y = y

    def getColor(self) : 
        if self.hp < 33 :
            return (255, 0, 0)
        elif self.hp < 66 :
            return (255, 255, 0)
        else :
            return (0, 255, 0)