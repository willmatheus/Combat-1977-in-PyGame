import pygame
from config import *
from pygame.locals import *
from sys import exit

pygame.init()

all_sprites = pygame.sprite.Group()
all_bricks_sprites = pygame.sprite.Group()


def main():
    # colors
    red = (162, 8, 0)
    yellow = (197, 199, 37)
    green = (0, 127, 33)

    # variables
    fps = 30
    game_clock = pygame.time.Clock()
    score_1 = 0
    score_2 = 0
    score_max = 3
    tank_1 = Tank()
    player_1 = 245

    # width and height of screen
    screen_width = 800
    screen_height = 600

    # screen size
    size = (screen_width, screen_height)
    player_x = 200
    player_y = 300

    # create the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Combat")

    all_sprites.add(tank_1)

    # create the game loop
    game_loop = True
    while game_loop:
        game_clock.tick(fps)
        screen.fill(red)

        # exit of game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if score_1 < score_max:
            tank_1.move()




        all_sprites.draw(screen)
        all_sprites.update()

        # wall upper
        pygame.draw.rect(screen, yellow, pygame.Rect(0, 100, 800, 20))
        # wall bottom
        pygame.draw.rect(screen, yellow, pygame.Rect(0, 580, 800, 20))
        # wall right
        pygame.draw.rect(screen, yellow, pygame.Rect(0, 100, 20, 600))
        # wall left
        pygame.draw.rect(screen, yellow, pygame.Rect(780, 100, 20, 600))
        # obstacles
        pygame.draw.rect(screen, yellow, pygame.Rect(400, 100, 50, 60))


        pygame.display.flip()


main()
