import pygame, sys
from button import Button
from gamestate import GameStateManager
from play import Game
from settings import Settings



pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("IQ GAME")

BG = pygame.image.load("game_images/space3.png")


def get_font(size):
    return pygame.font.Font("game_images/font.ttf", size)


def play():
    game_state_manager = GameStateManager()
    game = Game(SCREEN, game_state_manager)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()

        if game.game_state_manager.get_state() == 'menu':
            break

    pygame.display.update()
def options():
    game_state_manager = GameStateManager()
    settings = Settings(SCREEN, game_state_manager)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        settings.run()

        if settings.game_state_manager.get_state() == 'menu':
            break

        pygame.display.update()

    pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("IQ GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("game_images/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White",
                             click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
        OPTIONS_BUTTON = Button(image=pygame.image.load("game_images/Options Rect.png"), pos=(640, 400),
                                text_input="SETTINGS", font=get_font(70), base_color="#d7fcd4", hovering_color="White",
                                click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")
        QUIT_BUTTON = Button(image=pygame.image.load("game_images/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White",
                             click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
