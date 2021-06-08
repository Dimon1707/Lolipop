import pygame
import sys
import random


def drow_flor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


def crearte_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_serface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_serface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def drow_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_serface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_serface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_ract.colliderect(pipe):
            print('Ну всё гг')
            # death_soun.play()
            return False
        elif bird_ract.centery >= 1024 or bird_ract.centery <= 0:
            return False
    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


#def bird_animation():
#    new_bird = bird_frames[bird_index]
#    new_bird_ract = new_bird.getrect(center=(100, bird_ract.centery))
#    return new_bird, new_bird_ract


pygame.init()
screen = pygame.display.set_mode((575, 1024))
cloock = pygame.time.Clock()
font = pygame.font.Font('04B_19.TTF', 40)

# Игровая мехиника
gravity = 0.5
bird_movement = 0
game_active = True
score = 0
hightscore = 0

back_ground_surface = pygame.image.load('sprites/background-day.png').convert()
back_ground_surface = pygame.transform.scale2x(back_ground_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# bird_downflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-downflap.png')).convert_alpha()
# bird_midflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-midflap.png')).convert_alpha()
# bird_upflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-upflap.png')).convert_alpha()
# bird_frames = [bird_upflap, bird_midflap, bird_downflap]
# bird_index = 0

bird_surface = pygame.image.load('sprites/негр2.jpg').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_ract = bird_surface.get_rect(center=(100, 512))

pipe_serface = pygame.image.load('sprites/pipe-green.png').convert()
pipe_serface = pygame.transform.scale2x(pipe_serface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = 444, 600, 800

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_ract.center = (100, 512)
                bird_movement = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(crearte_pipe())
    screen.blit(back_ground_surface, (0, 0))
    if game_active:
        # ПТИЦА
        bird_movement += gravity
        bird_ract.centery += bird_movement
        screen.blit(bird_surface, bird_ract)
        game_active = check_collision(pipe_list)
        pipe_list = move_pipes(pipe_list)
        drow_pipes(pipe_list)
    floor_x_pos -= 1
    drow_flor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    screen.blit(floor_surface, (floor_x_pos, 900))
    pygame.display.update()
    cloock.tick(120)
pygame.quit()
