import pygame
import sys
from button import Button

class Settings:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.game_state_manager = gamestatemanager
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Option")
        self.FONT = pygame.font.Font("game_images/font.ttf", 50)
        self.volume = 50
        pygame.mixer.music.load('SOUND EFFECT AND BGM/QUIZ BG 2.wav')
        self.bg_image = pygame.image.load("game_images/space5.png")

    def adjust_volume(self, increment):
        self.volume = max(0, min(100, self.volume + increment))
        pygame.mixer.music.set_volume(self.volume / 100)

    def run(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.display.blit(self.bg_image, (0, 0))

            options_back = Button(image=None, pos=(640, 550),
                                  text_input="BACK", font=self.FONT, base_color="white", hovering_color="green",
                                  click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
            options_back.changeColor(OPTIONS_MOUSE_POS)
            options_back.update(self.SCREEN)

            volume_up = Button(image=None, pos=(640, 230),
                               text_input="Volume Up", font=self.FONT, base_color="white", hovering_color="green",
                               click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
            volume_up.changeColor(OPTIONS_MOUSE_POS)
            volume_up.update(self.SCREEN)

            volume_down = Button(image=None, pos=(640, 350),
                                 text_input="Volume Down", font=self.FONT, base_color="white", hovering_color="green",
                                 click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
            volume_down.changeColor(OPTIONS_MOUSE_POS)
            volume_down.update(self.SCREEN)

            volume_text = self.FONT.render(f"Volume: {self.volume}", True, "white")
            volume_rect = volume_text.get_rect(center=(640, 260))
            volume_rect.top = 55
            self.SCREEN.blit(volume_text, volume_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(OPTIONS_MOUSE_POS):
                        self.game_state_manager.set_state('menu')
                        return
                    if volume_up.checkForInput(OPTIONS_MOUSE_POS):
                        self.adjust_volume(1)
                    if volume_down.checkForInput(OPTIONS_MOUSE_POS):
                        self.adjust_volume(-1)

            pygame.display.update()
