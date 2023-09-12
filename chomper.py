import pygame
class Chomper(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.speed = 6
        self.direction = "right"
        self.starting_pos = (400, 400)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect(topleft=self.starting_pos)
        self.image.fill("blue")

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
        elif keys[pygame.K_UP]:
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.direction = "down"

    def move(self):
        if self.direction == "right":
            if self.rect.right < 1125:
                self.rect.x += self.speed
            else:
                self.direction = "left"
                self.game.lives.decrease_lives()
                if self.game.lives.lives == 0:
                    self.game.new_game = False
                    self.game.game_active = False
        elif self.direction == "left":
            if self.rect.left > 75:
                self.rect.x -= self.speed
            else:
                self.direction = "right"
                self.game.lives.decrease_lives()
                if self.game.lives.lives == 0:
                    self.game.new_game = False
                    self.game.game_active = False
        elif self.direction == "up":
            if self.rect.top > 75:
                self.rect.y -= self.speed
            else:
                self.direction = "down"
                self.game.lives.decrease_lives()
                if self.game.lives.lives == 0:
                    self.game.new_game = False
                    self.game.game_active = False
        elif self.direction == "down":
            if self.rect.bottom < 625:
                self.rect.y += self.speed
            else:
                self.direction = "up"
                self.game.lives.decrease_lives()
                if self.game.lives.lives == 0:
                    self.game.new_game = False
                    self.game.game_active = False

    def grow(self):
        self.size += 3
        current_x = self.rect.x
        current_y = self.rect.y
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(current_x, current_y))
        self.image.fill("blue")

    def increase_speed(self):
        self.speed += 1

    def update(self):
        self.move()
        self.change_direction()