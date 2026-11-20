import pygame

from code.const import SCR_WIDTH, GAME_OVER_OPTION


class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.title = pygame.image.load('./asset/Images/GameOver.png').convert_alpha()
        self.op_choice = pygame.mixer.Sound("./asset/Sounds/OpChoice.wav")
        self.op_select = pygame.mixer.Sound("./asset/Sounds/OpSelect.mp3")
        self.level_bg = pygame.image.load("./asset/Images/LevelBg.png").convert_alpha()
        self.title_position = self.title.get_rect(center=(SCR_WIDTH // 2, 200))
        self.font = pygame.font.SysFont(name="Verdana", size=45, bold=True)

    def run(self):
        game_over_option = 0
        pygame.mixer.music.load("./asset/Sounds/GameOver.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        while True:
            self.draw_game_over(game_over_option)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        game_over_option = (game_over_option + 1) % len(GAME_OVER_OPTION)
                        self.op_choice.set_volume(0.1)
                        self.op_choice.play()
                    elif event.key == pygame.K_UP:
                        game_over_option = (game_over_option - 1) % len(GAME_OVER_OPTION)
                        self.op_choice.set_volume(0.1)
                        self.op_choice.play()
                    elif event.key == pygame.K_RETURN:
                        self.op_select.set_volume(0.1)
                        self.op_select.play()
                        return GAME_OVER_OPTION[game_over_option]

            pygame.display.flip()

    def draw_game_over(self, game_over_option):
        self.screen.blit(self.level_bg, (0, 0))
        self.screen.blit(self.title, self.title_position)
        for i, option in enumerate(GAME_OVER_OPTION):
            if i == game_over_option:
                color = (255, 215, 0)
            else:
                color = (255, 255, 255)
            self.game_over_text(option, color, (SCR_WIDTH // 2, 360 + 80 * i))

    def game_over_text(self, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = self.font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(text_surf, text_rect)
