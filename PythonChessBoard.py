"""
PythonChessBoard: Setting up the board for use during the game
Author: Harrison Chebuk
Notes: a chess board is 8*8 and 64 squares total
"""


class GameTracker:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
        ]  # The starting board positions, from white perspective. R = rook, p = pawn, Q = queen and so on. color lead
        self.whitesTurn = True  # white always starts first

    def makeMove(self, move):
        self.board[move.firstRow][move.firstCol] = None
        self.board[move.lastRow][move.lastCol] = move.movedPiece
        self.whitesTurn = not self.whitesTurn  # flips turn


class MovePiece:
    """A class used to implement the movement"""
    def __init__(self, firstSquare, lastSquare, board):
        self.firstRow = firstSquare[0]
        self.firstCol = firstSquare[1]
        self.lastRow = lastSquare[0]
        self.lastCol = lastSquare[1]
        self.movedPiece = board[self.firstRow][self.firstCol]
        self.capturedPiece = board[self.lastRow][self.lastCol]



