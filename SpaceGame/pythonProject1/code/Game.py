#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.Part1 = None

    def run(self):

        while True:
            menu = Menu(self.window)

            menu.run()


