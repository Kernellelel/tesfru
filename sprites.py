import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.height = PLH
        self.width = PLW

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        #Arrow keys
        if keys[pygame.K_LEFT]:
            self.x_change -= SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += SPEED
            self.facing = 'down'
        #WASD
        if keys[pygame.K_a]:
            self.x_change -= SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += SPEED
            self.facing = 'down'

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = OBSTACLE
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.height = TILESIZE
        self.width = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button():
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect =  self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.screen.blit(self.image, self.rect)

    def checkInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
             print("check")

play_button = pygame.image.load('assets/play.png') 
play = Button(play_button, 300, 400)