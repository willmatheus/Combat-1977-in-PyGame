import pygame.sprite

from config import *
import layouts
from tank import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat-Atari")

tank_sprites = pygame.sprite.Group()
tank1 = Tank(tank_1, 40, 280, 0)
tank2 = Tank(tank_2, 730, 280, 8)
tank_sprites.add(tank1, tank2)

class Game():
    def __init__(self):
        pass

    # Check if an event happens
    def check_events(self):
        clk.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    tank1.rot_a()
                if event.key == pygame.K_d:
                    tank1.rot_d()
                if event.key == pygame.K_w:
                    tank1.move_w()
                if event.key == pygame.K_e:
                    tank1.shoot_()
                if event.key == pygame.K_k:
                    tank2.shoot_()
                if event.key == pygame.K_LEFT:
                    tank2.rot_a()
                if event.key == pygame.K_RIGHT:
                    tank2.rot_d()
                if event.key == pygame.K_UP:
                    tank2.move_w()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    tank1.no_rot_a()
                if event.key == pygame.K_d:
                    tank1.no_rot_d()
                if event.key == pygame.K_w:
                    tank1.no_move_w()
                if event.key == pygame.K_e:
                    tank1.no_shoot()
                if event.key == pygame.K_k:
                    tank2.no_shoot()
                if event.key == pygame.K_LEFT:
                    tank2.no_rot_a()
                if event.key == pygame.K_RIGHT:
                    tank2.no_rot_d()
                if event.key == pygame.K_UP:
                    tank2.no_move_w()

        for ball in tank1.ball_list:
            ball.move()
            ball.wall_collision(walls)
            if ball.cont == 3:
                tank1.ball_list.remove(ball)
                ball_sprites.remove(ball)

        for ball in tank2.ball_list:
            ball.move()
            ball.wall_collision(walls)
            if ball.cont == 3:
                tank2.ball_list.remove(ball)
                ball_sprites.remove(ball)

    # Select Layout
    def get_screen(self, layout_type):
        global background, walls

        layout = layouts.Layouts(layout_type)
        background = layout.get_bg_color()
        walls = layout.get_group()

    # Draws Elements
    def draw_sprites(self):
        global walls, background

        screen.fill(background)
        tank_sprites.draw(screen)
        tank_sprites.update()
        walls.draw(screen)
        ball_sprites.draw(screen)
        ball_sprites.update()



    def check_winner(self, tank_one, tank_two):
        global score_text_1, score_text_2

        if tank_one.score < SCORE_MAX and tank_two.score < SCORE_MAX:
            score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            screen.blit(score_text_1, score_text_1_rect)
            screen.blit(score_text_2, score_text_2_rect)

        else:
            if tank_two.score < tank_one.score:
                screen.fill(RED)
                score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
                screen.blit(victory_text1, victory_text_rect)
            elif tank_one.score < tank_two.score:
                screen.fill(RED)
                score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
                screen.blit(victory_text2, victory_text_rect)

    def game_loop(self):

        self.get_screen(1)

        while True:
            ball_collision(tank1, tank2)
            wall_collision(tank1, tank2)
            self.check_events()
            self.draw_sprites()
            self.check_winner(tank1, tank2)

            pygame.display.update()

            clk.tick(fps)


# score max
SCORE_MAX = 2

# score text
score_font = pygame.font.Font('font/Gamer.ttf', 90)
score_text_1 = score_font.render(f'{tank1.score}', True, GREEN)
score_text_2 = score_font.render(f'{tank2.score}', True, BLUE)
score_text_1_rect = (180, -15)
score_text_2_rect = (600, -15)

# victory text
victory_font = pygame.font.Font('font/Gamer.ttf', 100)
victory_text1 = victory_font.render('VICTORY PLAYER 1', True, YELLOW)
victory_text2 = victory_font.render('VICTORY PLAYER 2', True, YELLOW)
victory_text_rect = (110, 210)
