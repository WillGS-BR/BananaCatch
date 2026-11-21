import pygame

from code.const import SCR_WIDTH, SCR_HEIGHT, MENU_OPTION, GAME_OVER_OPTION
from code.game_over import GameOver
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        self.menu = Menu(self.screen)
        self.level = Level(self.screen)
        self.game_over = GameOver(self.screen)
        self.menu_option = MENU_OPTION
        self.game_over_option = GAME_OVER_OPTION

    def run(self):
        while True:
            menu_return = self.menu.run()
            match menu_return:
                case value if value == MENU_OPTION[0]:
                    self.level = Level(self.screen)
                    while True:
                        level_return = self.level.run()
                        game_over_return = self.game_over.run(level_return)
                        match game_over_return:
                            case value if value == GAME_OVER_OPTION[0]:
                                self.level = Level(self.screen)
                            case value if value == GAME_OVER_OPTION[1]:
                                break
                            case value if value == GAME_OVER_OPTION[2]:
                                pygame.quit()
                                quit()
                case value if value == MENU_OPTION[2]:
                    pygame.quit()
                    quit()
