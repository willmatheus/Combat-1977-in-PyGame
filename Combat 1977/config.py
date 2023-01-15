import pygame
from math import *
from pygame.locals import *
from sys import exit


# class tank
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/tank 1.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (32*4, 4*32))
        self.rect = self.image.get_rect()
        self.rect.topleft = 500, 100

    def move(self):
        if pygame.key.get_pressed()[K_a]:
            self.rect.x -= 5
        if pygame.key.get_pressed()[K_d]:
            self.rect.x += 5
        if pygame.key.get_pressed()[K_w]:
            self.rect.y -= 5
        if pygame.key.get_pressed()[K_s]:
            self.rect.y += 5
        if pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_w]:
            self.rect.move_ip(self.rect, )


