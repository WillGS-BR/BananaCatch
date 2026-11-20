import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import SCR_WIDTH, SCR_HEIGHT, MENU_OPTION


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.menuBg = pygame.image.load("./asset/Images/MenuBg.png").convert_alpha()
        self.title = pygame.image.load("./asset/Images/Title.png").convert_alpha()
        self.op_choice = pygame.mixer.Sound('./asset/Sounds/OpChoice.wav')
        self.op_select = pygame.mixer.Sound('./asset/Sounds/OpSelect.mp3')
        self.rect = self.title.get_rect(center = (SCR_WIDTH // 2, 160))

    def run(self):
        menu_op = 0
        pygame.mixer_music.load('./asset/Sounds/MenuMusic.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.blit(self.menuBg, (0, 0))
            self.screen.blit(self.title, self.rect)

            for i in range(len(MENU_OPTION)):
                if i == menu_op:
                    self.menu_text(60, MENU_OPTION[i], (255, 215, 0), (SCR_WIDTH / 2, 380 + 70 * i))
                else:
                    self.menu_text(60, MENU_OPTION[i], (255, 255, 255), (SCR_WIDTH / 2, 380 + 70 * i))

            pygame.display.flip()   # Update display

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_op < len(MENU_OPTION) - 1:
                            menu_op += 1
                        else:
                            menu_op = 0
                        self.op_choice.play()
                    if event.key == pygame.K_UP:
                        if menu_op > 0:
                            menu_op -= 1
                        else:
                            menu_op = len(MENU_OPTION) - 1
                        self.op_choice.play()
                    if event.key == pygame.K_RETURN:
                        self.op_select.play()
                        return MENU_OPTION[menu_op]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(text_surf, text_rect)
