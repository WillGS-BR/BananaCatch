import random

import pygame

from code.const import FALLING_SPEED


class Branch:
    def __init__(self):
        self.image = pygame.image.load("./asset/Images/Branch.png").convert_alpha()
        self.spawn = random.randint(40, 740)
        self.rect = self.image.get_rect(midtop=(self.spawn, -40))

    def move(self):
        self.rect.y += FALLING_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
