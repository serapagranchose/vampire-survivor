from game_loop import GameLoop
from os.path import join
from obstacle import Obstacle
from player import Player
from globals import *
import pygame
from os import listdir
from os.path import isfile, join

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

sprite_sheet_image = pygame.image.load('assets/characters/MiniNobleMan.png').convert_alpha()

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction = False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
            
        if direction:
            all_sprites[image.replace('.png', '') + '_right'] = sprites
            all_sprites[image.replace('.png', '') + '_left'] = flip(sprites)
        else:
            all_sprites[image.replace('.png', '')] = sprites
            
    return all_sprites

#player = Player(400, 500, 250, 250, pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)), sprite_sheet_image, load_sprite_sheets, flip)
space = pygame.Rect((0, 400, ZONE_WIDTH, ZONE_HEIGHT))
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

font.set_underline(True)
text = font.render('Hello Everyone!',True,(255,255,255))#This creates a new Surface with the specified text rendered on it
textrect = text.get_rect()
tmp = pygame.Rect((50, SCREEN_HEIGHT - 125, 50, 50))
pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)).bottomleft

gameloop = GameLoop(sprite_sheet_image, load_sprite_sheets, flip)
gameloop.addEnemy(Obstacle())
run = True
tick = 0
while run :
 
    tick = tick + 1 if tick < 1000 else 0

    gameloop.display(screen)

    res =  gameloop.tick(tick)
    if (res) : 
        break
  
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False

pygame.quit()

