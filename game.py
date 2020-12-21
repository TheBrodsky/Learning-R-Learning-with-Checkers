from board import Board
from cell import Cell


class Game:
    def __init__(self):
        self.board = Board()
        self.cur_turn = Cell.CellType.RED
        self.red_moves = {}
        self.black_moves = {}