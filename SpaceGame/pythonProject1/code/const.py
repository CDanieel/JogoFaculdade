# C
import pygame

COLLOR_ORANGE = (255, 128, 0)
COLLOR_YELLOW = (255, 255, 128)
COLLOR_WHITE = (255, 255, 255)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 1,
                'Level1BG2': 2,
                'Level1BG3': 3,
                'Level1BG4': 4,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
