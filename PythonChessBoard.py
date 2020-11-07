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


class MovePiece:
    """A class used to implement the drag and drop"""
    def __init__(self):
        pass


