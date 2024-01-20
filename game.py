from game_loop import GameLoop
from globals import *
from asyncio import sleep
from obstacle import Obstacle
from player import Player
import pygame
from os import listdir
from os.path import isfile, join

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
    
    pygame.display.update()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f'Score : ')
clock = pygame.time.Clock()

player = Player(pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)))
space = pygame.Rect((0, 400, ZONE_WIDTH, ZONE_HEIGHT))
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial
background, bg_image = get_background("plains.png")

font.set_underline(True)
text = font.render('Hello Everyone!',True,(255,255,255))#This creates a new Surface with the specified text rendered on it
textrect = text.get_rect()
tmp = pygame.Rect((50, SCREEN_HEIGHT - 125, 50, 50))
pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)).bottomleft

# space = pygame.Rect((0, 400, ZONE_WIDTH, ZONE_HEIGHT))
# font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

# font.set_underline(True)
# text = font.render('Hello Everyone!',True,(255,255,255))#This creates a new Surface with the specified text rendered on it
# textrect = text.get_rect()
gameloop = GameLoop()
gameloop.addEnemy(Obstacle())
run = True
tick = 0
while run :
    draw_background(screen, background, bg_image)
 
    # text = font.render(f'Score : {score}',True,(255,255,255))

    # screen.blit(text, textrect)
    tick = tick + 1 if tick < 1000 else 0

    # if (tick % 10) == 0 :
    #     for ob in obs :
    #         ob.update()
    #         if player.check_col(ob.entity) :
    #             run = True

    # if (tick == -1):
    #     obs.append(Obstacle())
    res =  gameloop.tick(tick)

    if (res) : 
        break

    # score = clean(score)
    # pygame.draw.rect(screen, (2, 2, 2), space)
   
    gameloop.display()
    
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

  
    


pygame.quit()

