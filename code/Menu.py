
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_BLUEF, MENU_OPTION, C_BLUE, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/backgroundmenu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/soundprinc.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, text="Get Way!", text_color= C_BLUEF, text_center_pos= ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_BLUE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()


            for event in pygame.event.get(): #EVENTO DE FECHAR A JANELA
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: #EVENTO DE APERTAR TECLA
                    if event.key == pygame.K_DOWN: #EVENTO SETA PARA BAIXO
                        if menu_option < len(MENU_OPTION)-1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: #EVENTO SETA PARA CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1

                    if event.key == pygame.K_RETURN:  # EVENTO DE SELECAO
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)