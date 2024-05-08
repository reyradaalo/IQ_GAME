import pygame
import sys
import random
from datetime import datetime, timedelta
from pygame.locals import *
from music import Music
from questions import EasyQuestion
from button import Button


class EasyGame:
    def __init__(self, display, gamestatemanager):
        self.active = False
        self.display = display
        self.game_state_manager = gamestatemanager
        self.background = pygame.image.load('game_images/space9 (1).png')
        self.start_background = pygame.image.load('game_images/space7 (1).png')
        self.game_over_background = pygame.image.load("game_images/space15 (1).png").convert()
        self.questions = EasyQuestion()
        self.game_over_sound_played = False

        self.current_question, self.correct_answer = self.questions.get_question()
        self.question_font = pygame.font.Font('game_images/font.ttf', 35)
        self.font = pygame.font.Font('game_images/font.ttf', 20)

        self.is_playing = False
        self.is_paused = False
        self.start_time = None
        self.paused_time = None
        self.timer_duration = timedelta(minutes=1, seconds=30)

        self.timer_pos = (10, 10)
        self.score = 0
        self.chances = 5
        self.chances_pos = (self.display.get_width() - 120, 20)

        self.music = Music()
        self.correct_answer_sound = pygame.mixer.Sound(self.music.correct_answer_path)
        self.wrong_answer_sound = pygame.mixer.Sound(self.music.wrong_answer_path)

        self.base_font = pygame.font.Font('game_images/font.ttf', 30)
        self.user_text = ""
        input_x = (self.display.get_width() - 350) // 2
        input_y = (self.display.get_height() - 32) // 2
        self.input_rect = pygame.Rect(input_x, input_y, 300, 32)
        self.color_active = pygame.Color(0, 0, 0)
        self.color_passive = pygame.Color(0, 0, 255)
        self.color = self.color_passive

        self.score_pos = (self.display.get_width() // 2, 20)
        self.asked_questions = set()

        self.timer_started = False
        self.start_message_displayed = False

        button_width = 100
        button_height = 50
        font_size = 30
        font = pygame.font.Font('game_images/font.ttf', font_size)
        self.back_button = Button(
            image=None,
            pos=(100, display.get_height() - button_height - 30),
            text_input="BACK",
            font=font,
            base_color=(255, 255, 255),
            hovering_color=(0, 255, 0),
            click_sound_path="SOUND EFFECT AND BGM/MOUSE CLICK.wav"
        )

    def reset_game(self):
        self.start_time = datetime.now()
        self.score = 0
        self.asked_questions.clear()
        self.user_text = ''
        self.chances = 5
        self.game_over_sound_played = False
        bg_music_path = random.choice([self.music.bg_music_path_1, self.music.bg_music_path_2])
        pygame.mixer.music.load(bg_music_path)
        pygame.mixer.music.play(-1)

        self.current_question, self.correct_answer = self.questions.get_question()

    def update_chances(self, decrement=True):
        if decrement:
            if self.chances > 0:
                self.chances -= 1
        else:
            self.chances = 5
            self.reset_game()

    def started_game(self):
        self.is_playing = True
        self.start_time = datetime.now()

    def draw_popup_message(self, message):
        popup_font = pygame.font.Font('game_images/font.ttf', 40)
        popup_text = popup_font.render(message, True, (255, 255, 255))
        popup_rect = popup_text.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 2))
        self.display.blit(popup_text, popup_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def show_score_popup(self):
        score_message = f"Your Score: {self.score}"
        popup_font = pygame.font.Font('game_images/font.ttf', 40)
        popup_text = popup_font.render(score_message, True, (255, 255, 255))
        popup_rect = popup_text.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 4))
        self.display.blit(popup_text, popup_rect)
        pygame.display.flip()

    def handle_button_click(self, pos):
        if self.back_button.is_clicked(pos):
            self.game_state_manager.set_state('play')
            return

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.back_button.is_clicked(event.pos):
                            self.game_state_manager.set_state('play')
                            return

                        if self.input_rect.collidepoint(event.pos):
                            self.active = True
                        else:
                            self.active = False

                if event.type == pygame.KEYDOWN:
                    if not self.is_playing and event.key == pygame.K_SPACE:
                        self.started_game()
                        self.start_message_displayed = True

                    if self.active:
                        if event.key == K_RETURN:
                            if self.is_playing and not self.is_paused:
                                if self.user_text.strip() == str(self.correct_answer):
                                    self.score += 1
                                    if self.score % 10 == 0:
                                        self.chances += 2
                                    if self.score % 15 == 0:
                                        self.chances += 4
                                    if self.score % 20 == 0:
                                        self.chances += 6
                                    self.timer_duration += timedelta(seconds=10)
                                    self.current_question, self.correct_answer = self.questions.get_question()
                                    self.user_text = ''
                                    self.correct_answer_sound.play()
                                else:
                                    self.wrong_answer_sound.play()
                                    self.update_chances()

                        elif event.key == K_END:
                            self.reset_game()
                            if self.game_state_manager:
                                self.game_state_manager.set_state('play')

                        elif event.key == K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text += event.unicode

                if self.active:
                    self.color = self.color_active
                else:
                    self.color = self.color_passive

            if not self.is_playing:
                if not self.start_message_displayed:
                    self.display.blit(self.start_background, (0, 0))
                    start_message_font = pygame.font.Font('game_images/font.ttf', 36)
                    start_message_text = start_message_font.render("Press SPACE to start", True, (255, 255, 255))
                    start_message_rect = start_message_text.get_rect()
                    start_message_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)
                    self.display.blit(start_message_text, start_message_rect)
                    pygame.display.flip()
                    continue

            if self.is_playing:
                elapsed_time = datetime.now() - self.start_time
                remaining_time = max(self.timer_duration - elapsed_time, timedelta(seconds=0))
                game_over_sound = pygame.mixer.Sound('SOUND EFFECT AND BGM/GAME OVER.wav')

                if not self.timer_started and self.score > 0:
                    self.start_time = datetime.now()
                    self.timer_started = True

                if remaining_time == timedelta(seconds=0):
                    pygame.mixer.music.stop()
                    game_over_sound.play()
                    self.game_over_sound_played = True

                    self.display.fill((0, 0, 0))
                    game_over_text = self.font.render("Time's up! Game Over", True, (255, 0, 0))
                    game_over_rect = game_over_text.get_rect(
                        center=(self.display.get_width() // 2, self.display.get_height() // 2))
                    self.display.blit(game_over_text, game_over_rect)
                    self.show_score_popup()

                    main_menu_text = self.font.render("Try Again", True, (255, 255, 255))
                    exit_text = self.font.render("Exit", True, (255, 255, 255))
                    main_menu_rect = main_menu_text.get_rect(
                        center=(self.display.get_width() // 2, self.display.get_height() // 2 + 40))
                    exit_rect = exit_text.get_rect(
                        center=(self.display.get_width() // 2, self.display.get_height() // 2 + 80))

                    self.display.blit(main_menu_text, main_menu_rect)
                    self.display.blit(exit_text, exit_rect)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_m:
                                pygame.mixer.music.stop()
                                self.reset_game()
                                if self.game_state_manager:
                                    self.game_state_manager.set_state('play')
                            elif event.key == K_b:
                                pygame.quit()
                                sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if main_menu_rect.collidepoint(event.pos):
                                self.reset_game()
                                if self.game_state_manager:
                                    self.game_state_manager.set_state('play')
                            elif exit_rect.collidepoint(event.pos):
                                pygame.quit()
                                sys.exit()

            else:
                remaining_time = self.timer_duration

            game_over_sound = pygame.mixer.Sound('SOUND EFFECT AND BGM/GAME OVER.wav')
            if self.chances == 0:
                if not self.game_over_sound_played:
                    pygame.mixer.music.stop()
                    game_over_sound.play()
                    self.game_over_sound_played = True

                self.display.blit(self.game_over_background, (0, 0))
                game_over_text = self.font.render("Game Over", True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(
                    center=(self.display.get_width() // 2, self.display.get_height() // 2))
                self.display.blit(game_over_text, game_over_rect)
                self.show_score_popup()

                main_menu_text = self.font.render("Try Again", True, (255, 255, 255))
                exit_text = self.font.render("Exit", True, (255, 255, 255))
                main_menu_rect = main_menu_text.get_rect(
                    center=(self.display.get_width() // 2, self.display.get_height() // 2 + 40))
                exit_rect = exit_text.get_rect(
                    center=(self.display.get_width() // 2, self.display.get_height() // 2 + 80))

                self.display.blit(main_menu_text, main_menu_rect)
                self.display.blit(exit_text, exit_rect)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_m:
                            pygame.mixer.music.stop()
                            self.reset_game()
                            if self.game_state_manager:
                                self.game_state_manager.set_state('play')
                        elif event.key == K_b:
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if main_menu_rect.collidepoint(event.pos):
                            self.reset_game()
                            if self.game_state_manager:
                                self.game_state_manager.set_state('play')
                        elif exit_rect.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

                pygame.time.Clock().tick(60)
                continue

            self.display.fill((0, 0, 0))
            self.display.blit(self.background, (0, 0))

            question_surface = self.font.render(self.current_question, True, (255, 255, 255))
            question_rect = question_surface.get_rect(center=(self.display.get_width() // 2, 250))
            self.display.blit(question_surface, question_rect)

            pygame.draw.rect(self.display, self.color, self.input_rect)
            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.input_rect.center)
            self.display.blit(text_surface, text_rect)

            timer_surface = self.font.render("Timer: " + str(remaining_time), True, (255, 255, 255))
            self.display.blit(timer_surface, self.timer_pos)

            score_text = f"Score: {self.score}"
            score_surface = self.font.render(score_text, True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=self.score_pos)
            self.display.blit(score_surface, score_rect)

            chances_text = f"Chances: {self.chances}"
            chances_surface = self.font.render(chances_text, True, (255, 255, 255))
            chances_rect = chances_surface.get_rect(center=self.chances_pos)
            self.display.blit(chances_surface, chances_rect)

            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.input_rect.center)

            self.display.blit(text_surface, text_rect)
            self.display.blit(score_surface, score_rect)
            self.display.blit(chances_surface, chances_rect)

            self.input_rect.w = max(300, text_surface.get_width())

            self.back_button.draw(self.display)

            pygame.display.flip()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((1280, 720))
    game = EasyGame(display, None)
    game.run()
