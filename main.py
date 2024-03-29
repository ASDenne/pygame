import time
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((1000,740))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("snake game - by andrew denne")

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (188, 227, 199)
yellow = (255,255,0)
blue = (0,0,255)
score_font = pygame.font.SysFont("arialblack",20)
exit_font = pygame.font.Font("freesansbold.ttf",30)
msg_font = pygame.font.SysFont("arialblack",20)
clock = pygame.time.Clock()

def draw_snake(snake_list,colour):
    #print(f"snake list:{snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen,colour,[i[0],i[1],20, 20])

def message(msg,txt_colour,bkgd_colour):
    txt = msg_font.render(msg,True,txt_colour,bkgd_colour)

    text_box = txt.get_rect(center=(500,360))
    screen.blit(txt,text_box)

def game_loop():
    quit_game = False
    game_over = False
    size_x = 1000
    size_y = 720
    screen = pygame.display.set_mode((size_x,size_y))
    snake_x = size_x/2-10
    snake_y = size_y/2-10
    snake_list = []
    snake_length = 1
    speed = 5

    snake_x_change = 0
    snake_y_change = 0

    food_x = round(random.randrange(20,1000 - 20)/20)*20
    food_y = round(random.randrange(20,720 - 20)/20)*20

    while not quit_game:

        while game_over:
            screen.fill(white)
            message("you died! press 'Q' to quit or 'A' to play Again",
                    black, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to quit, SPACE to resume, R to reset"
                message(instructions,white,black)
                pygame.display.update()
                end = False
                while not end:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()
                            if event.key == pygame.K_SPACE:
                                end = True
                            if event.key == pygame.K_x:
                                quit_game = True
                                end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_y_change = 0
                    snake_x_change = -20
                elif event.key == pygame.K_RIGHT:
                    snake_y_change = 0
                    snake_x_change = 20
                elif event.key == pygame.K_UP:
                    snake_y_change = -20
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = 20
                    snake_x_change = 0

        if snake_x >= size_x or snake_x < 0 or snake_y >= size_y or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        snake_head = [snake_x,snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        draw_snake(snake_list,red)
        draw_snake([snake_head],blue)
        pygame.display.update()


        pygame.draw.circle(screen,yellow,[food_x,food_y],10)
        pygame.display.update()

        if snake_x == food_x -10 and snake_y == food_y - 10:
            food_x = round(random.randrange(20,size_x - 40)/20)*20
            food_y = round(random.randrange(20,size_y - 40)/20)*20
            snake_length += 1
            size_y = size_y-20
            size_x = size_x-20
            speed += -0.1
            screen = pygame.display.set_mode((size_x,size_y))

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
