import unittest as ut
from board import Board
from cell import Cell


class BoardTests(ut.TestCase):
    def setUp(self):
        self.board = Board()

    def test_BoardSetupSize(self):
        self.assertEqual(len(self.board.board), 8)
        self.assertEqual(len(self.board.board[1]), 8)

    def test_BoardSetupInitialCells(self):
        self.assertEqual(self.board.board[0][0].type, Cell.CellType.EMPTY)
        self.assertEqual(self.board.board[0][1].type, Cell.CellType.BLACK)
        self.assertEqual(self.board.board[1][0].type, Cell.CellType.BLACK)
        self.assertEqual(self.board.board[3][0].type, Cell.CellType.EMPTY)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.EMPTY)
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)
        self.assertEqual(self.board.board[6][1].type, Cell.CellType.RED)


if __name__ == "__main__":
    ut.main()
