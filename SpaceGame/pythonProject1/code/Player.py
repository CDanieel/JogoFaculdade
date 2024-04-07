#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()  # ele verifica se a tecla ESTÁ sendo pressionada

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Se a tecla para cima foi pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]  # ele verifica se a tecla ESTÁ sendo pressionada

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Se a tecla para baixo foi pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se a tecla para esquerda foi pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Se a tecla para direita foi pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]


