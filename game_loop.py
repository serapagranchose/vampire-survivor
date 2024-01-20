from math import *
import pygame
from globals import *
from obstacle import Obstacle
from player import Player


class GameLoop : 
    def __init__(self) :
        self.enemy = []
        self.player = Player(pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock =  pygame.time.Clock()
        self.fps = 120
        self.offset = pygame.math.Vector2(0, 0)


    def addEnemy(self, enemy) :
        self.enemy.append(enemy)
    

    def tick(self, tick) :
        key = pygame.key.get_pressed()
        self.move(key)
        
        if (len(self.enemy) < 10) : 
            self.addEnemy(Obstacle())

        if tick % 8 is 0 :
            for enemy in self.enemy : 
                enemy.updatePos(self.offset)
            self.getDammage()
            self.kill()

    def move(self, key) :
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            self.offset[1] += 1
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            self.offset[1] -= 1
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            self.offset[0] += 1
        if key[pygame.K_d] == True  or key[pygame.K_RIGHT] == True:
            self.offset[0] -= 1


    def display(self) : 
        pygame.display.update()
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, self.player.color, self.player.entity)
        for enemy in self.enemy :
            pygame.draw.rect(self.screen, enemy.getColor(), enemy.entity)
        self.clock.tick(self.fps)

    def getDammage(self) : 
        py, px =  SCREEN_WIDTH/2 - self.offset[0] , SCREEN_HEIGHT/2 - self.offset[1]
        for enemy in self.enemy : 
            dist =  sqrt((enemy.entity.x - px)**2 + (enemy.entity.y - py)**2)
            if (dist < 150) : 
                enemy.hp -= 5

    def kill(self) : 
        toRemove = []
        for enemy in self.enemy:
            if enemy.hp <= 0:
                self.enemy.remove(enemy)
     


            