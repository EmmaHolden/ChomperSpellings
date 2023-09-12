import pygame

pygame.init()

spelling_words = ["camel", "otter", "octopus", "sealion", "tiger"]

game_font = pygame.font.Font('font/Pixeltype.ttf', 60)

instruction_font = pygame.font.Font('font/Pixeltype.ttf', 40)

word_font = pygame.font.Font('font/Pixeltype.ttf', 80)

game_colours = {
    "green": '#00DFA2',
    "blue": '#0079FF',
    "yellow": '#F6FA70',
    "orange": '#FF9526',
    "red": '#FF0060',
    "purple": '#2A3492',
}

x_coordinates = [110, 170, 230, 290, 350, 410, 470, 530, 590, 650, 710, 770, 830, 890, 950, 1010, 1070]

y_coordinates = [100, 160, 220, 280, 340, 400, 460, 520, 580]

