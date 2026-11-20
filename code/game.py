from code.const import SCR_WIDTH, SCR_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        self.menu = Menu(self.screen)

    def run(self):
        menu_return = self.menu.run()
        if menu_return == MENU_OPTION[0]:
            level = Level(self.screen)
            level_return = level.run()
        if menu_return == MENU_OPTION[1]:
            pass
        if menu_return == MENU_OPTION[2]:
            pygame.quit()
            quit()
