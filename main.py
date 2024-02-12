import time

import pygame
pygame.init()

screen = pygame.display.set_mode((1000,720))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("snake game - by andrew denne")

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (188, 227, 199)
score_font = pygame.font.SysFont("arialblack",20)
exit_font = pygame.font.Font("freesansbold.ttf",30)
quit_game = False

snake_x = 490
snake_y = 350

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    pygame.draw.rect(screen,red,[snake_x,snake_y,20,20])
    pygame.display.update()

pygame.quit()
quit()
