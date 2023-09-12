import pygame
import random
from game_variables import game_font

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.letter = self.random_incorrect_letter()
        self.image = game_font.render(self.letter, False, 40)
        self.location = random.choice(self.game.coordinates)
        self.game.coordinates.remove(self.location)
        self.rect = self.image.get_rect(topleft = self.location)

    def random_incorrect_letter(self):
        self.enemy_letters_unicode = [i for i in range(65, 90) if i != ord(self.game.spelling_word[self.game.current_letter_index])]
        return chr(random.choice(self.enemy_letters_unicode))

    def update_letter(self):
        self.image = self.image = game_font.render(self.random_incorrect_letter(), False, 40)