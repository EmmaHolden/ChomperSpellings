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
            self.game.score.increase_score()
            if self.game.current_letter_index < len(self.game.spelling_word):
                self.handle_food_collision()
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

    def check_teleporter_collision(self):
        collisions =  pygame.sprite.groupcollide(self.chomper, self.teleporter_group, False, False)
        if collisions:
            coordinates = []
            for teleporter in self.teleporter_group:
                coordinates.append(teleporter.coordinates)
            random_coordinates_found = False
            while not random_coordinates_found:
                random_coordinates = random.choice(coordinates)
                if not random_coordinates[0] - 30 < self.chomper.sprite.rect.x < random_coordinates[0] + 30 and not random_coordinates[1] - 30 < self.chomper.sprite.rect.y < random_coordinates[1] + 30:
                    random_coordinates_found = True
            if random_coordinates[0] == 85:
                self.chomper.sprite.direction = "right"
                self.chomper.sprite.rect.x = random_coordinates[0] + 50
                self.chomper.sprite.rect.y = random_coordinates[1]
            elif random_coordinates[0] == 1125:
                self.chomper.sprite.direction = "left"
                self.chomper.sprite.rect.x = random_coordinates[0] - 50
                self.chomper.sprite.rect.y = random_coordinates[1]
            elif random_coordinates[1] == 85:
                self.chomper.sprite.direction = "down"
                self.chomper.sprite.rect.x = random_coordinates[0]
                self.chomper.sprite.rect.y = random_coordinates[1] + 50
            else:
                self.chomper.sprite.direction = "up"
                self.chomper.sprite.rect.x = random_coordinates[0]
                self.chomper.sprite.rect.y = random_coordinates[1] - 50


    def handle_food_collision(self):
        self.chomper.sprite.grow()
        self.chomper.sprite.increase_speed()
        self.food.sprite.relocate_food()

    def update(self):
        self.check_food_collision()
        self.check_enemy_collision()
        self.check_teleporter_collision()