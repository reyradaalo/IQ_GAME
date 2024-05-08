import pygame
from button import Button
from medium import MediumGame
from easy import EasyGame
from hard import HardGame


class Game:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.game_state_manager = gamestatemanager
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Play")
        self.background = pygame.image.load("game_images/space4 (1).png").convert()

    def get_font(self, size):
        return pygame.font.Font("game_images/font.ttf", size)

    def run(self):
        while True:
            self.SCREEN.blit(self.background, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            button_height = 100

            total_button_height = 4 * button_height + 3 * 10

            start_y = (self.SCREEN.get_height() - total_button_height) // 2

            button_positions = [(640, start_y),
                                (640, start_y + button_height + 20),
                                (640, start_y + 2 * (button_height + 20)),
                                (640, start_y + 3 * (button_height + 40))]

            buttons = [
                Button(image=None, pos=button_positions[0], text_input="EASY", font=self.get_font(100),
                       base_color="White", hovering_color="Green",
                       click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav"),
                Button(image=None, pos=button_positions[1], text_input="MEDIUM", font=self.get_font(100),
                       base_color="White", hovering_color="Green",
                       click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav"),
                Button(image=None, pos=button_positions[2], text_input="HARD", font=self.get_font(100),
                       base_color="White", hovering_color="Green",
                       click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav"),
                Button(image=None, pos=button_positions[3], text_input="BACK", font=self.get_font(50),
                       base_color="White", hovering_color="Green",
                       click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
            ]

            for button in buttons:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.checkForInput(PLAY_MOUSE_POS):
                            if button.text_input == "EASY":
                                easy_game = EasyGame(self.display, self.game_state_manager)
                                easy_game.run()
                            elif button.text_input == "MEDIUM":
                                medium_game = MediumGame(self.display, self.game_state_manager)
                                medium_game.run()
                            elif button.text_input == "HARD":
                                hard_game = HardGame(self.display, self.game_state_manager)
                                hard_game.run()
                            elif button.text_input == "BACK":
                                self.game_state_manager.set_state('menu')
                                return

            pygame.display.update()
