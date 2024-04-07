#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLLOR_ORANGE, MENU_OPTION, COLLOR_WHITE, COLLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        #pygame.mixer.init()
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            # Desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Space", (COLLOR_ORANGE), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Game", (COLLOR_ORANGE), ((WIN_WIDTH / 2), 100))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:  # ELE E RESPONSAVEL PARA MUDAR A COR QUANDO SE SELICIONA NO MENU.
                    self.menu_text(20, MENU_OPTION[i], COLLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            #  Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # testar se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # se a tecla para BAIXO foi pressionada
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # se a seta para CIMA foi pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        pygame.init()
        pygame.font.Font()
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
