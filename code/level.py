import pygame

from code.banana import Banana
from code.const import SPAWN_TIME, EVENT_BANANA
from code.monkey import Monkey


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.monkey = Monkey()
        self.banana_list = []
        self.level_bg = pygame.image.load("./asset/Images/LevelBg.png").convert_alpha()
        pygame.time.set_timer(EVENT_BANANA, SPAWN_TIME)

    def run(self):
        pygame.mixer.music.load("./asset/Sounds/LevelMusic.wav")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.screen.blit(self.level_bg, (0, 0))
            self.monkey.move()
            for banana in self.banana_list:
                banana.move()
            self.monkey.draw(self.screen)
            for banana in self.banana_list:
                banana.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_BANANA:
                    self.banana_list.append(Banana())
