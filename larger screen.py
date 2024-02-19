import time
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((1000,740))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("snake game - by andrew denne")
#colours
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (148, 227, 159)
yellow = (255,255,0)
blue = (0,0,255)

score_font = pygame.font.SysFont("arialblack",20)
exit_font = pygame.font.Font("freesansbold.ttf",30)
msg_font = pygame.font.SysFont("arialblack",20)
clock = pygame.time.Clock()

def update_high_score(score,high_score):
    #print(score)
    #print(high_score)
    if int(score)>int(high_score):
        return score
    else:
        return high_score

def load_high_score():
    #getting hi scroe from file
    try:
        hi_score_file = open("HI_score.txt",'r')
    except IOError:
        hi_score_file = open("HI_score.txt",'w')
        hi_score_file.write("0")
    hi_score_file =open("HI_score.txt",'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value

def save_high_score(high_score):
    #saving high scores
    high_score_file = open("HI_score.txt",'w')
    high_score_file.write(str(high_score))
    high_score_file.close()

def player_score(score,score_colour,hi_score):
    #deslpaying scores
    display_score = score_font.render(f"score: {score}",True,score_colour)
    screen.blit(display_score,(10,10))
    display_score = score_font.render(f"high score: {hi_score}",True,score_colour)
    screen.blit(display_score,(10,30))

def draw_snake(snake_list,colour):
    #drawing each square in a snake
    #print(f"snake list:{snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen,colour,[i[0],i[1],10, 10])

def message(msg,txt_colour,bkgd_colour,x,y):
    #sending a pause or end of game message
    txt = msg_font.render(msg,True,txt_colour,bkgd_colour)

    text_box = txt.get_rect(center=(x,y))
    screen.blit(txt,text_box)

def game_loop():
    #the game
    #stats
    quit_game = False
    game_over = False
    size_x = 1000
    size_y = 720
    screen = pygame.display.set_mode((size_x,size_y))
    snake_x = size_x/2-5
    snake_y = size_y/2-5
    snake_list = []
    snake_length = 1
    speed = 5
    temp_speed = speed
    score = 0

    snake_x_change = 0
    snake_y_change = 0

    food_x = round(random.randrange(10,1000 - 10)/10)*10
    food_y = round(random.randrange(10,720 - 10)/10)*10

    high_score = load_high_score()
    print(f"high_score test: {high_score}")

    while not quit_game:
        #screen = pygame.display.set_mode((1000,720))
        while game_over:
            save_high_score(high_score)
            #screen = pygame.display.set_mode((1000,720))
            screen.fill(white)
            message("you died! press 'Q' to quit or 'A' to play Again",
                    black, white,size_x/2,size_y/2)
            pygame.display.update()
#see what the directions are
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #screen = pygame.display.set_mode((1000,720))
                instructions = "Exit: X to quit, SPACE to resume, R to reset"
                message(instructions,white,black,size_x/2,size_y/2)
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
                if event.key == pygame.K_w:
                    temp_speed = speed*3
                elif event.key == pygame.K_s:
                    temp_speed = speed/2
                else:
                    temp_speed = speed
                if event.key == pygame.K_LEFT and not (snake_y_change == 0 and snake_x_change == 10):
                    snake_y_change += 0
                    snake_x_change += -10
                if event.key == pygame.K_RIGHT and not (snake_y_change == 0 and snake_x_change == -10):
                    snake_y_change += 0
                    snake_x_change += 10
                if event.key == pygame.K_UP and not (snake_y_change == 10 and snake_x_change == 0):
                    snake_y_change += -10
                    snake_x_change += 0
                if event.key == pygame.K_DOWN and not (snake_y_change == -10 and snake_x_change == 0):
                    snake_y_change += 10
                    snake_x_change += 0
                if snake_x_change > 10:
                    snake_x_change = 10
                if snake_y_change > 10:
                    snake_y_change = 10
                if snake_x_change < -10:
                    snake_x_change = -10
                if snake_y_change < -10:
                    snake_y_change = -10
        if snake_x >= size_x:
            snake_x = 5
        if snake_y >= size_y:
            snake_y = 5
        if snake_x < 0:
            snake_x = size_x-5
        if snake_y < 0:
            snake_y = size_y-5

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
        #pygame.display.update()
        score = snake_length -1
        high_score = update_high_score(score,high_score)
        player_score(score,black,high_score)

        #pygame.draw.circle(screen,yellow,[food_x,food_y],5)
        food =pygame.Rect(food_x-5,food_y-5,10,10)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple,[10,10])
        screen.blit(resized_apple,food)
        pygame.display.update()

        if snake_x == food_x-5 and snake_y == food_y-5 :
            food_x = round(random.randrange(10,size_x - 10)/10)*10
            food_y = round(random.randrange(10,size_y - 10)/10)*10
            snake_length += 1
            size_y = size_y-10
            size_x = size_x-10
            speed += 0.1
            screen = pygame.display.set_mode((size_x,size_y))

        clock.tick(temp_speed)

    pygame.quit()
    quit()

game_loop()
