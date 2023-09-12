import random
import pygame
from game_variables import game_colours, x_coordinates, y_coordinates, spelling_words, game_font
from itertools import product
from chomper import Chomper
from food import Food
from teleporter import Teleporter
class GameOver():
    def __init__(self, game, enemy_group, food, chomper, teleport_group):
        self.game = game
        self.enemy_group = enemy_group
        self.food = food
        self.chomper = chomper
        self.teleport_group = teleport_group

    def welcome_screen(self):
        self.game.screen_setup.screen.fill(game_colours["orange"])
        self.game.screen_setup.screen.blit(self.game.screen_setup.title, (500, 70))
        self.game.screen_setup.screen.blit(self.game.screen_setup.start_instructions, (370, 520))
        for i in range(0, len(self.game.screen_setup.game_instruction_surfaces)):
            self.game.screen_setup.screen.blit(self.game.screen_setup.game_instruction_surfaces[i], self.game.screen_setup.game_instruction_coordinates[i])
        self.game.score.get_score(coordinates = (490, 600))


    def handle_game_over(self):
        self.game.screen_setup.screen.fill(game_colours["orange"])
        self.game.screen_setup.screen.blit(self.game.screen_setup.start_instructions, (300, 300))
        self.game.screen_setup.screen.blit(self.game.screen_setup.title, (500, 70))
        self.game.score.get_score(coordinates=(490, 600))
        if self.game.lives.lives < 1:
            self.game.screen_setup.screen.blit(self.game.screen_setup.lose_message, (300, 400))
        else:
            self.game.screen_setup.screen.blit(self.game.screen_setup.win_message, (300, 400))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game.new_game = True

    def restart_game(self):
        self.game.coordinates = list(product(x_coordinates, y_coordinates))
        self.game.spelling_word = random.choice(spelling_words).upper()
        for enemy in self.enemy_group:
            enemy.kill()
        for teleport in self.teleport_group:
            teleport.kill()
        self.food.sprite.kill()
        self.chomper.sprite.kill()
        self.game.current_letter_index = 0
        self.game.lives.lives = 3
        self.teleport_group.add(Teleporter("left", self.game))
        self.teleport_group.add(Teleporter("right", self.game))
        self.teleport_group.add(Teleporter("top", self.game))
        self.teleport_group.add(Teleporter("bottom", self.game))
        self.food.add(Food(self.game))
        self.chomper.add(Chomper(self.game))
        self.game.timer = 180
        self.game.spelling_word_shown = False
        self.game.game_active = True
