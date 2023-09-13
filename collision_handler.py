import pygame
from enemy import Enemy
import random

class CollisionHandler():

    def __init__(self, game, enemy_group, chomper, food, teleporter_group, game_over):
        self.game = game
        self.game_over = game_over
        self.enemy_group = enemy_group
        self.chomper = chomper
        self.food = food
        self.teleporter_group = teleporter_group
    def check_food_collision(self):
        if pygame.sprite.groupcollide(self.chomper, self.food, False, False):
            self.game.current_letter_index += 1
            self.game.score.increase_score(10)
            if self.game.current_letter_index < len(self.game.spelling_word):
                self.chomper.sprite.grow()
                self.chomper.sprite.increase_speed(1)
                self.food.sprite.relocate_food()
                for item in self.enemy_group:
                    if item.letter == self.game.spelling_word[self.game.current_letter_index]:
                        item.update_letter()
                self.enemy_group.add(Enemy(self.game))
            else:
                self.game.new_game = False
                self.game.game_active = False

    def check_enemy_collision(self):
        collision = pygame.sprite.groupcollide(self.chomper, self.enemy_group, False, True)
        if collision:
            self.chomper.sprite.harmful_collision()

    def check_which_teleporter(self):
        for teleporter in self.teleporter_group:
            if teleporter.rect.colliderect(self.chomper.sprite.rect):
                return teleporter

    def find_new_x_coordinate(self, teleporter):
        if self.chomper.sprite.direction == "up" or self.chomper.sprite.direction == "down":
            return teleporter.opposite.rect.x
        elif self.chomper.sprite.direction == "left":
            return teleporter.opposite.rect.x - 50
        elif self.chomper.sprite.direction == "right":
            return teleporter.oppposite.rect.x + 50

    def check_teleporter_collision(self):
        collisions =  pygame.sprite.groupcollide(self.chomper, self.teleporter_group, False, False)
        if collisions:
            self.game.score.increase_score(2)
            self.chomper.sprite.increase_speed(0.25)
            teleporter = self.check_which_teleporter()
            self.chomper.sprite.direction = teleporter.position
            self.chomper.sprite.rect.x = self.chomper.sprite.find_new_x_coordinate(teleporter)
            self.chomper.sprite.rect.y = self.chomper.sprite.find_new_y_coordinate(teleporter)


    def update(self):
        self.check_food_collision()
        self.check_enemy_collision()
        self.check_teleporter_collision()