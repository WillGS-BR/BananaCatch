import sys

import pygame

from code.const import SCR_WIDTH, MENU_OPTION


class Menu:
    def __init__(self, screen):
        self.screen = screen
        # Images
        self.menu_bg = pygame.image.load("./asset/Images/MenuBg.png").convert_alpha()
        self.title = pygame.image.load("./asset/Images/Title.png").convert_alpha()
        self.controls = pygame.image.load("./asset/Images/Controls.png").convert_alpha()
        # Sounds
        self.op_choice = pygame.mixer.Sound("./asset/Sounds/OpChoice.wav")
        self.op_select = pygame.mixer.Sound("./asset/Sounds/OpSelect.mp3")
        # Positions
        self.title_position = self.title.get_rect(center=(SCR_WIDTH // 2, 160))
        self.controls_position = self.controls.get_rect(center=(SCR_WIDTH // 2, 160))
        # Settings
        self.font = pygame.font.SysFont(name="Verdana", size=45, bold=True)
        self.clock = pygame.time.Clock()

    def run(self):
        menu_option = 0
        show_controls = False
        pygame.mixer.music.load("./asset/Sounds/MenuMusic.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        while True:
            self.clock.tick(60)
            if show_controls:
                self.draw_controls()
            else:
                self.draw_menu(menu_option)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if show_controls:
                        if event.key == pygame.K_RETURN:
                            show_controls = False
                            self.op_select.play()
                    else:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            menu_option = (menu_option + 1) % len(MENU_OPTION)
                            self.op_choice.set_volume(0.1)
                            self.op_choice.play()
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            menu_option = (menu_option - 1) % len(MENU_OPTION)
                            self.op_choice.set_volume(0.1)
                            self.op_choice.play()
                        elif event.key == pygame.K_RETURN:
                            self.op_select.set_volume(0.1)
                            self.op_select.play()
                            if menu_option == 1:
                                show_controls = True
                            else:
                                return MENU_OPTION[menu_option]

    def draw_menu(self, menu_option):
        self.screen.blit(self.menu_bg, (0, 0))
        self.screen.blit(self.title, self.title_position)

        for i, option in enumerate(MENU_OPTION):

            if i == menu_option:
                color = (255, 215, 0)
            else:
                color = (255, 255, 255)

            self.menu_text(option, color, (SCR_WIDTH // 2, 360 + 80 * i))

    def draw_controls(self):
        self.screen.blit(self.menu_bg, (0, 0))
        self.screen.blit(self.controls, self.controls_position)
        self.menu_text("A - Move Left", (255, 255, 255), (SCR_WIDTH // 2, 300))
        self.menu_text("D - Move Right", (255, 255, 255), (SCR_WIDTH // 2, 370))
        self.menu_text("BACK", (255, 215, 0), (SCR_WIDTH // 2, 500))

    def menu_text(self, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = self.font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(text_surf, text_rect)
