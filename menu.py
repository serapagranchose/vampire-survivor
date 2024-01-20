from globals import *
import pygame
import button

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

font.set_underline(True)

pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)).bottomleft

def main_menu():
    run = True

    play_img = pygame.image.load("./assets/buttons/menu/large/regular/Play.png").convert_alpha()
    play_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Play.png").convert_alpha()
    button_scale = (play_img.get_height() / SCREEN_HEIGHT) * 2

    button_space = play_img.get_height() * 0.75
    play_button_height = (SCREEN_HEIGHT / 4)
    play_button = button.Button(SCREEN_WIDTH * 0.5, play_button_height, play_img, play_img_colored, button_scale)
    play_button.selected = True

    settings_img = pygame.image.load("./assets/buttons/menu/large/regular/Settings.png").convert_alpha()
    settings_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Settings.png").convert_alpha()
    settings_button_height = play_button_height + button_space
    settings_button = button.Button(SCREEN_WIDTH * 0.5, settings_button_height, settings_img, settings_img_colored, button_scale)

    quit_img = pygame.image.load("./assets/buttons/menu/large/regular/Quit.png").convert_alpha()
    quit_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Quit.png").convert_alpha()
    quit_button_height = settings_button_height + button_space
    quit_button = button.Button(SCREEN_WIDTH * 0.5, quit_button_height, quit_img, quit_img_colored, button_scale)

    buttons = [play_button, settings_button, quit_button]
    selected_index = 0

    while run:
        screen.fill((0,0,0))
        
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                run = False
            if(event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_DOWN):
                    buttons[selected_index].selected = False
                    selected_index += 1
                    if (selected_index > len(buttons) - 1):
                        selected_index = 0
                    buttons[selected_index].selected = True
                if (event.key==pygame.K_UP):
                    buttons[selected_index].selected = False
                    selected_index -= 1
                    if (selected_index < 0):
                        selected_index = len(buttons) - 1
                    buttons[selected_index].selected = True

        for menu_button in buttons:
            action = menu_button.draw(screen)
            if (action and quit_button.selected == True):
                run = False
            if (action and play_button.selected == True):
                pass


        pygame.display.update()


main_menu()

pygame.quit()

