import pygame
class Chomper(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.hurt_timer = 0
        self.hurt = False
        self.game = game
        self.speed = 4
        self.direction = "right"
        self.size = 50
        self.image = pygame.image.load('graphics/chomper.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(400, 400))


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
                self.harmful_collision()
        elif self.direction == "left":
            if self.rect.left > 75:
                self.rect.x -= self.speed
            else:
                self.direction = "right"
                self.harmful_collision()
        elif self.direction == "up":
            if self.rect.top > 75:
                self.rect.y -= self.speed
            else:
                self.direction = "down"
                self.harmful_collision()
        elif self.direction == "down":
            if self.rect.bottom < 625:
                self.rect.y += self.speed
            else:
                self.direction = "up"
                self.hurt = True
                self.harmful_collision()

    def find_new_x_coordinate(self, teleporter):
        if teleporter.opposite.position == "up" or teleporter.opposite.position == "down":
            return teleporter.opposite.rect.x
        elif teleporter.opposite.position == "left":
            return teleporter.opposite.rect.x + 50
        elif teleporter.opposite.position == "right":
            return teleporter.opposite.rect.x - 50

    def find_new_y_coordinate(self, teleporter):
        if teleporter.opposite.position == "left" or teleporter.opposite.position == "right":
            return teleporter.opposite.rect.y
        elif teleporter.opposite.position == "up":
            return teleporter.opposite.rect.y + 50
        elif teleporter.opposite.position == "down":
            return teleporter.opposite.rect.y - 50

    def harmful_collision(self):
        self.game.lives.decrease_lives()
        if self.game.lives.lives == 0:
            self.game.new_game = False
            self.game.game_active = False
        self.hurt = True
        self.increase_speed(5)
        self.image = pygame.transform.scale(self.image, (self.size + 10, self.size + 10))
    def timed_injury(self):
        self.hurt_timer += 1
        if self.hurt_timer > 25:
            self.hurt_timer = 0
            self.hurt = False
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.decrease_speed(5)

    def grow(self):
        self.size += 3
        current_x = self.rect.x
        current_y = self.rect.y
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(current_x, current_y))

    def increase_speed(self, amount):
        self.speed += amount

    def decrease_speed(self, amount):
        self.speed -= amount

    def update(self):
        self.move()
        self.change_direction()