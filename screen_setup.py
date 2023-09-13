import pygame
from game_variables import game_font, instruction_font, word_font, timer_font, game_colours
class ScreenSetup():
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((1200, 700))
        self.background = pygame.Surface((1200, 700))
        self.background.fill(game_colours["green"])
        self.play_grid = pygame.Surface((1050, 550))
        self.play_grid.fill(game_colours["yellow"])
        self.title = game_font.render('Chomper', False, "black")
        self.start_instructions = game_font.render('Press Space Bar to Play', False, 100)
        self.game_instructions = ['Move the chomper around the screen to catch the letters.',
                                  'Be careful of enemy letters sent to confuse you!',
                                  'Pressing space bar stops the game and lets you hear the word.',
                                  'Purple teleporters give extra points but make the chomper faster.',
                                  'Do not touch the walls!'
                                  ]
        self.game_instruction_surfaces = []
        self.game_instruction_coordinates = [(230, 140), (300, 220), (320, 300), (280, 380), (420, 460)]
        for sentence in self.game_instructions:
            render = instruction_font.render(sentence, False, 50)
            self.game_instruction_surfaces.append(render)
        self.time_message = game_font.render('Oops! You ran out of time!', False, "black")
        self.lose_message = game_font.render('Oops! You ran out of lives!', False, "black")
        self.win_message = game_font.render('Well done! You got all of the letters!', False, "black")

    def get_game_timer(self):
        timer_display = game_font.render(f'{round(self.game.game_timer / 60)}', False, "black")
        self.game.screen_setup.screen.blit(timer_display, (160, 20))
        self.game.game_timer -= 1
        if self.game.game_timer <= 0:
            self.game.game_active = False
            self.game.new_game = False


    def get_hurt_timer(self):
        timer_display = timer_font.render(f'{round(self.game.hurt_timer / 60)}', False, "black")
        self.game.screen_setup.screen.blit(timer_display, (500, 500))
        self.game.hurt_timer -= 1
        if self.game.hurt_timer < 0:
            self.game.spelling_word_shown = True

    def get_spelling_word(self):
        self.spelling_word_display_title = game_font.render("Spelling Word: ", False, "black")
        self.spelling_word_display = word_font.render(f'{self.game.spelling_word}', False, "black")
        self.screen.blit(self.spelling_word_display_title, (400, 200))
        self.screen.blit(self.spelling_word_display, (450, 350))


    def reveal_word(self):
        self.revealed_letters = self.game.spelling_word[0:self.game.current_letter_index]
        self.word_surface= game_font.render("Word:", False, "black")
        self.revealed_letter_surface = game_font.render(self.revealed_letters, False, game_colours["yellow"])
        self.screen.blit(self.word_surface, (700, 645))
        self.screen.blit(self.revealed_letter_surface, (820, 645))

    def update(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.play_grid, (75, 75))
        self.screen.blit(self.title, (520, 20))
        self.reveal_word()
        self.get_game_timer()
