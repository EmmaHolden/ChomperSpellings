import pygame
import random
from sys import exit
from itertools import product
from game_variables import game_font, game_colours, x_coordinates, y_coordinates, spelling_words
from chomper import Chomper
from food import Food
from collision_handler import CollisionHandler
from scorekeeper import Scorekeeper
from screen_setup import ScreenSetup
from teleporter import Teleporter
from lives import Lives
from game_over import GameOver
import pyttsx3

class GameSetup():
    def __init__(self):
        self.timer = 180
        self.game_active = False
        self.new_game = True
        self.coordinates = list(product(x_coordinates, y_coordinates))
        self.spelling_word_shown = False
        self.spelling_word = random.choice(spelling_words).upper()
        self.current_letter_index = 0
        self.screen_setup = ScreenSetup(self)
        self.score = Scorekeeper(self)
        self.lives = Lives(self)
    def update(self):
        self.screen_setup.update()
        self.score.get_score(coordinates = (350, 645))
        self.lives.get_lives_display()

pygame.init()
text_speech = pyttsx3.init()
pygame.display.set_caption("Spelling Chomper Game")
clock = pygame.time.Clock()
game = GameSetup()
chomper = pygame.sprite.GroupSingle()
chomper.add(Chomper(game))
food = pygame.sprite.GroupSingle()
food.add(Food(game))
enemy_group = pygame.sprite.Group()
teleport_group = pygame.sprite.Group()
game_over = GameOver(game, enemy_group, food, chomper, teleport_group)
collision_handler = CollisionHandler(game, enemy_group, chomper, food, teleport_group, game_over)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if game.game_active == False:
                    if game.new_game:
                        game_over.restart_game()
                else:
                    text_speech.say(game.spelling_word)
                    text_speech.runAndWait()
    if game.game_active:
        if chomper.sprite.hurt == True:
            chomper.sprite.deal_with_injury()
        if game.spelling_word_shown:
            game.update()
            chomper.draw(game.screen_setup.screen)
            food.draw(game.screen_setup.screen)
            chomper.update()
            collision_handler.update()
            enemy_group.draw(game.screen_setup.screen)
            teleport_group.draw(game.screen_setup.screen)
        else:
            game.screen_setup.screen.fill(game_colours["red"])
            game.screen_setup.get_spelling_word()
            game.screen_setup.get_timer()
    else:
        if game.new_game:
            game_over.welcome_screen()
        else:
            game_over.handle_game_over()

    pygame.display.update()
    clock.tick(60)
