from game_loop import GameLoop
from game_loop import GameLoop
from os.path import join
from obstacle import Obstacle
from player import Player
from globals import *
from player import Player
from pause_menu import pause_menu
import pygame
from os import listdir
from os.path import isfile, join


# def clean(score):
#     for ob in obs:
#         if ob.entity.bottom >= (SCREEN_HEIGHT) :
#             obs.remove(ob)
#             score += 1
#     return score

# pygame.display.set_caption(f'Score : ')

score = 0

# space = pygame.Rect((0, 400, ZONE_WIDTH, ZONE_HEIGHT))
# font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

# font.set_underline(True)
# text = font.render('Hello Everyone!',True,(255,255,255))#This creates a new Surface with the specified text rendered on it
# textrect = text.get_rect()
def launch_game(screen, sprite_sheet_image, load_sprite_sheets, flip):
    gameloop = GameLoop(sprite_sheet_image, load_sprite_sheets, flip)
    gameloop.addEnemy(Obstacle())
    run = True
    tick = 0
    while run :
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
        gameloop.tick(tick)



        # score = clean(score)
        # pygame.draw.rect(screen, (2, 2, 2), space)
    
        gameloop.display(screen)
        
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if pause_menu(gameloop.screen):
                        run = False
