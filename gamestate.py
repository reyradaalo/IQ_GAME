import pygame.time
from music import Music


class GameStateManager:
    def __init__(self, initial_state='menu'):
        self.states = initial_state
        self.current_state = initial_state
        self.previous_state = initial_state
        self.clock = pygame.time.Clock()
        self.running = True

        self.musics_load = Music()

        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.mixer.init()

        pygame.mixer.music.load(self.musics_load.bg_music_path_2)
        pygame.mixer.music.play(-1)

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def set_state(self, state_name):
        self.previous_state = self.current_state
        self.current_state = state_name

    def get_state(self):
        return self.current_state

    def switch_to_previous_state(self):
        if self.previous_state is not None:
            self.current_state, self.previous_state = self.previous_state, self.current_state
