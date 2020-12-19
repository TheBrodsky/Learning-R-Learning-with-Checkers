import unittest as ut
from board import Board
from cell import Cell


class BoardTests(ut.TestCase):
    def setUp(self):
        self.board = Board()

    def test_BoardSetup(self):
        self.assertEqual(len(self.board.board), 8)
        self.assertEqual(len(self.board.board[1]), 8)
        self.assertEqual(self.board.board[0][0].type, Cell.CellType.EMPTY)


if __name__ == "__main__":
    ut.main()
