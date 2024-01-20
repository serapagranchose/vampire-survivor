from math import *
import pygame
from background import Background
from globals import *
from obstacle import Obstacle
from player import Player
from shoot import Bullet


red = 255,0,0


class GameLoop : 
    def __init__(self) :
        self.enemy = []
        self.player = Player(pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock =  pygame.time.Clock()
        self.fps = 120
        self.offset = pygame.math.Vector2(0, 0)
        self.background = Background()


    def addEnemy(self, enemy) :
        self.enemy.append(enemy)
    

    def tick(self, tick) :
        res = False
        key = pygame.key.get_pressed()
        self.move(key)
        
        if (len(self.enemy) < MAX_ENEMY) : 
            self.addEnemy(Obstacle())

        if tick % 8 is 0 :
            for enemy in self.enemy : 
                enemy.updatePos(self.offset)
                res = self.player.check_col(enemy.entity)
                if (res) : 
                    break
            self.getDammage()
            self.kill()
        return res
            

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
        self.display_background()
        pygame.draw.rect(self.screen, self.player.color, self.player.entity)
        for enemy in self.enemy :
            pygame.draw.rect(self.screen, enemy.getColor(), enemy.entity)
        self.clock.tick(self.fps)
      

    def display_background(self) :
        for tile in self.background.tiles:
            self.screen.blit(self.background.image, tuple(map(lambda i, j: i + j, tile, (self.offset[0], self.offset[1]))))

    def getDammage(self) : 
        for enemy in self.enemy : 
            dist =  sqrt((enemy.x - ( SCREEN_WIDTH/2 - self.offset[0]))**2 + (enemy.y - ( SCREEN_HEIGHT/2 - self.offset[1]))**2)
            if (dist < 150) : 
                enemy.hp -= 5

    def kill(self) : 
        for enemy in self.enemy:
            if enemy.hp <= 0:
                self.enemy.remove(enemy)

    def create_bullet(self) :
        Bullet(red, 2, 2, 20,20, 20, 10,10)
     


            