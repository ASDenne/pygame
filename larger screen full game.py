import time
import random
import pygame
pygame.init()
global time
global space
global space_time
global time_time
time = False
space = False
space_time = 0
time_time = 0
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
cyan = (0,255,255)
fruit_plain = green
fruit_time = yellow
fruit_space = cyan
#feature locked or require certain things for when not testing while be behind a if testing
testing = True
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
        if space and random.randint(0,3)==2:
            pygame.draw.rect(screen,fruit_space,[i[0],i[1],10, 10])
        if time and random.randint(0,5)==1:
            pygame.draw.rect(screen,fruit_time,[i[0],i[1],10, 10])


def message(msg,txt_colour,bkgd_colour,x,y):
    #sending a pause or end of game message
    txt = msg_font.render(msg,True,txt_colour,bkgd_colour)

    text_box = txt.get_rect(center=(x,y))
    screen.blit(txt,text_box)

def game_loop():
    #the game
    #stats
    time = False
    space = False
    space_time = 0
    time_time = 0
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
    food_count = 5
    snake_x_change = 0
    snake_y_change = 0
    food_x = []
    food_y = []
    food_type = []
    for i in range(food_count):
        food_x.append(round(random.randrange(10,1000 - 10)/10)*10)
        food_y.append(round(random.randrange(10,720 - 10)/10)*10)
        food_type.append(random.choices(["normal","space","time"],[5,1,1]))
        print(food_type)

    high_score = load_high_score()
    #print(f"high_score test: {high_score}")
    screensizeupdate = True
    while not quit_game:
        print(space)
        print(time)
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
                #if they click the X
                #screen = pygame.display.set_mode((1000,720))
                instructions = "Exit: X to quit, SPACE to resume, R to reset"
                message(instructions,white,black,size_x/2,size_y/2)
                pygame.display.update()
                end = False
                while not end:
                    #seeing which command is given
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
            #seeing what keys are being pressed for directions
            # (take out + to set it to just left right up down and not diagonal
            if event.type == pygame.KEYDOWN:
                if testing or time:
                    if event.key == pygame.K_w:
                        temp_speed = speed*5
                    elif event.key == pygame.K_s:
                        temp_speed = speed/4
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
                #limiting increases of movement to 1x and 1y square per turn
                if not space:
                    if snake_x_change > 10:
                        snake_x_change = 10
                    if snake_y_change > 10:
                        snake_y_change = 10
                    if snake_x_change < -10:
                        snake_x_change = -10
                    if snake_y_change < -10:
                        snake_y_change = -10
        #setting up screen wrapping so that snake reaches other side
        if snake_x >= size_x:
            snake_x = -5
        if snake_y >= size_y:
            snake_y = -5
        if snake_x < -5:
            snake_x = size_x+5
        if snake_y < -5:
            snake_y = size_y+5

        snake_x += snake_x_change
        snake_y += snake_y_change
        if screensizeupdate:
                    screen = pygame.display.set_mode((size_x,size_y))
                    screensizeupdate = False
        screen.fill(green)
        #printing the snake
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
        # setting up and printing scores
        score = snake_length -1
        high_score = update_high_score(score,high_score)
        player_score(score,black,high_score)
        #printing food
        for i in range(food_count):
        #pygame.draw.circle(screen,yellow,[food_x,food_y],5)
            if food_type[i-1] == ["space"]:
                pygame.draw.circle(screen,fruit_space,[food_x[i-1],food_y[i-1]],7)
            elif food_type[i-1] == ["time"]:
                pygame.draw.circle(screen,fruit_time,[food_x[i-1],food_y[i-1]],7)
            food = pygame.Rect(food_x[i-1]-5,food_y[i-1]-5,10,10)
            apple = pygame.image.load('apple_3.png').convert_alpha()
            resized_apple = pygame.transform.smoothscale(apple,[10,10])
            screen.blit(resized_apple,food)


            #pygame.display.update()
            #spawning food

            if snake_x == food_x[i-1]-5 and snake_y == food_y[i-1]-5 :
                food_x[i-1] = round(random.randrange(10,size_x - 10)/10)*10
                food_y[i-1] = round(random.randrange(10,size_y - 10)/10)*10
                snake_length += 1
                size_y = size_y-10
                size_x = size_x-10
                screensizeupdate = True
                speed += 0.1
                if food_type[i-1] == ["space"]:
                    space_time += 30
                    space = True
                elif food_type[i-1] == ["time"]:
                    time_time += 30
                    time = True
                #screen = pygame.display.set_mode((size_x,size_y))
                #screen.fill(green)
            if size_x < food_x[i-1]-5 or size_y < food_y[i-1]-5 :
                food_x[i-1] = round(random.randrange(10,size_x - 10)/10)*10
                food_y[i-1] = round(random.randrange(10,size_y - 10)/10)*10
        #screen = pygame.display.set_mode((size_x,size_y))

        pygame.display.update()

        #print(food_x)
        #print(food_y)
        #print(size_x)
        #print(size_y)
        #print()
        clock.tick(temp_speed)

    pygame.quit()
    quit()
#starting loop
game_loop()
