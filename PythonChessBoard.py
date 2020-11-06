"""
PythonChessBoard: Setting up the board for use during the game
Author: Harrison Chebuk
Notes: a chess board is 8*8 and 64 squares total
"""

import pygame
from pygame.locals import *


class ChessMain:
    tilesize = 100

    def __init__(self, width=640, height=480):
        white, black = (255, 255, 255), (0, 0, 0)
        pygame.init()
        self.window = pygame.display.set_mode((width, height))




