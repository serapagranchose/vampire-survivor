from game_loop import GameLoop
from os.path import join
from obstacle import Obstacle
from globals import *
import pygame

pygame.init()

score = 0

# def clean(score):
#     for ob in obs:
#         if ob.entity.bottom >= (SCREEN_HEIGHT) :
#             obs.remove(ob)
#             score += 1
#     return score

def get_background(name):
    image = pygame.image.load(join("assets", "backgrounds", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(SCREEN_WIDTH // width + 1):
        for j in range(SCREEN_HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw_background(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
    

background, bg_image = get_background("plains.png")

gameloop = GameLoop()
gameloop.addEnemy(Obstacle())
run = True
tick = 0
while run :
 
    tick = tick + 1 if tick < 1000 else 0

    gameloop.display()
    draw_background(gameloop.screen, background, bg_image)
    
    res =  gameloop.tick(tick)
    if (res) : 
        break
  
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

  
    


pygame.quit()

