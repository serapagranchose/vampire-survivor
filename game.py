from globals import *
from asyncio import sleep
from obstacle import Obstacle
from player import Player
import pygame

pygame.init()

score = 0

def clean(score):
    for ob in obs:
        if ob.entity.bottom >= (SCREEN_HEIGHT) :
            obs.remove(ob)
            score += 1
    return score

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f'Score : ')
clock = pygame.time.Clock()

player = Player(pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)))
space = pygame.Rect((0, 400, ZONE_WIDTH, ZONE_HEIGHT))
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

font.set_underline(True)
text = font.render('Hello Everyone!',True,(255,255,255))#This creates a new Surface with the specified text rendered on it
textrect = text.get_rect()
tmp = pygame.Rect((50, SCREEN_HEIGHT - 125, 50, 50))
pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)).bottomleft


run = True
tick = 0
obs = []

while run :
    screen.fill((0,0,0))
    text = font.render(f'Score : {score}',True,(255,255,255))

    screen.blit(text, textrect)
    tick = tick + 1 if tick < 30 else 0

    if (tick % 10) == 0 :
        for ob in obs :
            ob.update()
            if player.check_col(ob.entity) :
                run = False

    if (tick == 0):
        obs.append(Obstacle())
    player.move(pygame.key.get_pressed())

    score = clean(score)
    pygame.draw.rect(screen, (2, 2, 2), space)
    for ob in obs : 
        pygame.draw.rect(screen, ob.color, ob.entity)
    
    pygame.draw.rect(screen, (255, 0, 0), player.entity)

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

  
    pygame.display.update()

    clock.tick(180)

print(score)
pygame.quit()

