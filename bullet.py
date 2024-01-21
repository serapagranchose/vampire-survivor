import pygame, math, random,time

from globals import PROJ_COLOR


class Bullet:
    def __init__(self, x, y, width, height, speed, targetx,targety):
        self.rect = pygame.Rect(x, y, width, height)
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, PROJ_COLOR, self.rect)

    def check_shoot(self, enemy):
        if  ((
            self.rect.right <= enemy.entity.right and self.rect.right >= enemy.entity.left
             ) or (self.rect.left >= enemy.entity.left and self.rect.left <= enemy.entity.right
                   )) and ((self.rect.top >= enemy.entity.top and self.rect.top <= enemy.entity.bottom
                       ) or (self.rect.bottom <= enemy.entity.bottom and self.rect.bottom >= enemy.entity.top)): 
            enemy.hp -= 5
            return True
        return False
