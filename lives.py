import pygame
from game_variables import game_font

class Lives():
    def __init__(self, game):
        self.game = game
        self.lives = 3
    def get_lives_display(self):
        self.lives_image = pygame.image.load(f'graphics/heart{self.lives}.png').convert_alpha()
        self.game.screen_setup.screen.blit(self.lives_image, (800, 10))

    def decrease_lives(self):
        self.lives -= 1
