import pygame

from code.const import SCR_WIDTH, MONKEY_SPEED


class Monkey:
    def __init__(self):
        self.image = pygame.image.load("./asset/Images/Monkey.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCR_WIDTH // 2, 560))

    def move(self):
        speed = MONKEY_SPEED
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and self.rect.right < SCR_WIDTH:
            speed = MONKEY_SPEED + 2
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[pygame.K_d] and self.rect.right < SCR_WIDTH:
            self.rect.x += speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
