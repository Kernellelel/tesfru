import pygame
import sys
from config import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

    def new(self):
        self.createTileMap()
        self.playing = True
        self.attacks = pygame.sprite.LayeredUpdates()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             self.playing = False
             self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
             play.checkInput(pygame.mouse.get_pos())
             play.update()
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        pygame.display.update()
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    def end(self):
        pass
    def intro(self):
        pass

game = Game()
game.new()
while game.running:
    game.main()

sys.exit()