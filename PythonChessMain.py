"""
Chess main where we will update board state and run the game.
Author: Harrison Chebuk
Sources: Many many different pygame tutorials - pygame official help from github - etc. - a snake game was used as ex.
https://www.pygame.org/docs/index.html
Notes: A chess is 8 by 8
"""

import pygame as board
from PythonChessBoard import *
import os
import math

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") # the path to the images folder in comp
width = 512 # pixel size of window
height = 512
tileSize = width // 8 # a chess board is 8x8, we calculate pixel size of squares by this
img = {}  # dictionary of our images
brown, light_brown = (102, 51, 0), (153, 102, 51)  # RGB values for brown and light brown, to be used on tiles


def imageLoader():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for p in pieces:
        img[p] = board.transform.scale(board.image.load("{}/pieces/{}.png".format(THIS_FOLDER, p)), (tileSize, tileSize))


def drawBoard(screen, tracker):
    """update the board squares and draw pieces on top of tiles"""
    for row in range(8):
        for col in range(8):
            color = (row + col) % 2  # we can calculate what color based on this, because the color pattern shift by 1 as we go down
            if color == 0:
                board.draw.rect(screen, light_brown, board.Rect(col * tileSize, row * tileSize, tileSize, tileSize))
            else:
                board.draw.rect(screen, brown, board.Rect(col * tileSize, row * tileSize, tileSize, tileSize))
            # draw a piece on top of a tile, (blit draws a single image on top of something)
            piece = tracker[row][col]
            if piece is not None:
                screen.blit(img[piece], board.Rect(col * tileSize, row * tileSize, tileSize, tileSize))


def main():
    board.mixer.init()
    board.init()
    screen = board.display.set_mode((width, height))
    clock = board.time.Clock()
    tracker = GameTracker()  # keeps track of the game
    imageLoader()
    running = True
    board.mixer.music.load("{}/music/music.mp3".format(THIS_FOLDER))  # loading in the jams
    board.mixer.music.play(loops=-1)
    curSquare = ()  # (row, col)
    clickTrack = []  # [curSquare, curSquare]
    while running:  # our game loop

        for i in board.event.get():
            if i.type == board.QUIT:  # running loop ends
                running = False
            elif i.type == board.MOUSEBUTTONDOWN:
                mouseLocation = board.mouse.get_pos()  # the location of the mouse on the screen x, y
                row = mouseLocation[1]//tileSize
                col = mouseLocation[0] // tileSize
                curSquare = (row, col)
                clickTrack.append(curSquare)
                if len(clickTrack) == 2:  # second click occurred
                    move = MovePiece(clickTrack[0], clickTrack[1], tracker.board)
                    tracker.makeMove(move)
                    curSquare = ()  # reset the click
                    clickTrack.clear()
        drawBoard(screen, tracker.board) # update our moves
        clock.tick(60)  # FPS per tick of gametime, use minecraft commands to remember lol
        board.display.flip()  # updates the contents of the entire display
    board.mixer.music.stop()
    board.mixer.quit()


if __name__ == '__main__':
    main()



