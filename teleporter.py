import pygame
import random
from game_variables import game_colours
class Teleporter(pygame.sprite.Sprite):
    def __init__(self, position, game):
        super().__init__()
        self.game = game
        self.position = position
        self.coordinates = self.get_coordinates()
        self.width = self.get_width()
        self.length = self.get_length()
        self.image = pygame.Surface((self.width, self.length))
        self.rect = self.image.get_rect(center=self.coordinates)
        self.image.fill(game_colours["purple"])

    def get_opposite(self, opposite):
        self.opposite = opposite
        opposite.opposite = self
    def get_width(self):
        if self.position == "right" or self.position == "left":
            return 20
        else:
            return 100

    def get_length(self):
        if self.position == "right" or self.position == "left":
            return 100
        else:
            return 20
    def get_coordinates(self):
        if self.position == "left":
            return (85, self.get_random_coordinate(200, 500))
        elif self.position == "right":
            return (1125, self.get_random_coordinate(200, 500))
        elif self.position == "up":
            return (self.get_random_coordinate(200, 1000), 85)
        elif self.position == "down":
            return (self.get_random_coordinate(200, 1000), 615)
    def get_random_coordinate(self, lower, upper):
        return random.randint(lower, upper)

