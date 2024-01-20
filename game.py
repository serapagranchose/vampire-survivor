from game_loop import GameLoop
from os.path import join
from obstacle import Obstacle
from globals import *
import pygame

pygame.init()


gameloop = GameLoop()
gameloop.addEnemy(Obstacle())
run = True
tick = 0
while run :
 
    tick = tick + 1 if tick < 1000 else 0

    gameloop.display()
    
    res =  gameloop.tick(tick)
    if (res) : 
        break
  
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

pygame.quit()

