import pygame
from game_variables import game_font
class Scorekeeper():
    def __init__(self, game):
        self.game = game
        self.score = 0
    def get_score(self, coordinates):
        self.score_display = game_font.render(f'Score:  {self.score}', False, "black")
        self.game.screen_setup.screen.blit(self.score_display, coordinates)
    def increase_score(self, amount):
        self.score += amount

