import pygame
from gamestate import GameStateManager
from menu import Menu
from settings import Settings
from play import Game
from medium import MediumGame
from easy import EasyGame
from hard import HardGame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('IQ Game')

game_state_manager = GameStateManager(initial_state='start')

game_state_manager.add_state('start', Menu(screen, game_state_manager))
game_state_manager.add_state('play', Game(screen, game_state_manager))
game_state_manager.add_state('settings', Settings(screen, game_state_manager))
game_state_manager.add_state('normal', MediumGame(screen, game_state_manager))
game_state_manager.add_state('easy', EasyGame(screen, game_state_manager))
game_state_manager.add_state('hard', HardGame(screen, game_state_manager))

while game_state_manager.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state_manager.running = False

    game_state_manager.run_current_state(screen)

    pygame.display.flip()

    game_state_manager.clock.tick(60)

pygame.quit()
