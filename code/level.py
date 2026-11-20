import random

import pygame

from code.banana import Banana
from code.branch import Branch
from code.const import SPAWN_TIME, EVENT_BANANA, SCR_HEIGHT, SCR_WIDTH, GAME_OVER_OPTION
from code.game_over import GameOver
from code.menu import Menu
from code.monkey import Monkey


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.monkey = Monkey()
        self.lives = 3
        self.banana_list = []
        self.branch_list = []
        self.level_bg = pygame.image.load("./asset/Images/LevelBg.png").convert_alpha()
        self.game_over_title = pygame.image.load("./asset/Images/GameOver.png").convert_alpha()
        self.collect_sound = pygame.mixer.Sound('./asset/Sounds/Collect.mp3')
        self.damage_sound = pygame.mixer.Sound('./asset/Sounds/Damage.mp3')
        pygame.time.set_timer(EVENT_BANANA, SPAWN_TIME)

    def run(self):
        pygame.mixer.music.load("./asset/Sounds/LevelMusic.wav")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.screen.blit(self.level_bg, (0, 0))
            self.monkey.draw(self.screen)
            self.monkey.move()

            for banana in self.banana_list[:]:
                banana.draw(self.screen)
                banana.move()
                if self.monkey.rect.colliderect(banana.rect):
                    self.banana_list.remove(banana)
                    self.collect_sound.set_volume(0.2)
                    self.collect_sound.play()
                if banana.rect.top > SCR_HEIGHT:
                    self.banana_list.remove(banana)
                    self.lives -= 1
                    self.damage_sound.set_volume(0.2)
                    self.damage_sound.play()
            for branch in self.branch_list[:]:
                branch.draw(self.screen)
                branch.move()
                if self.monkey.rect.colliderect(branch.rect):
                    self.branch_list.remove(branch)
                    self.lives -= 1
                    self.damage_sound.set_volume(0.2)
                    self.damage_sound.play()

            pygame.display.flip()
            if self.lives == 0:
                self.lives = 3
                return 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_BANANA:
                    if random.randint(1, 10) == 1:
                        self.branch_list.append(Branch())
                    else:
                        self.banana_list.append(Banana())


