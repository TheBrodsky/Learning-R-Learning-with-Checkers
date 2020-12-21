import unittest as ut
from game import Game
from board import Board
from cell import Cell

class GameTests(ut.TestCase):
    def setUp(self):
        pass

    def test_CannotMoveMoreThanOneSpaceUnlessJump(self):
        pass

    def test_CannotMoveToNegativeIndexSpace(self):
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)
        self.board.move(5, 0, 4, -1)
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)

    def test_CannotMoveBackwardIfNotKinged(self):
        self.board.move(5, 0, 4, 1)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.RED)
        self.board.move(4, 1, 5, 0)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.RED)
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.EMPTY)

    def test_CanMoveBackwardIfKinged(self):
        self.board.move(5, 0, 4, 1)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.RED)
        self.board.king_cell(4, 1)
        self.board.move(4, 1, 5, 0)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.EMPTY)
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)

    def test_CannotMoveToFriendlySpace(self):
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)
        self.board.king_cell(5, 0)  # used to differentiate the 2 cells
        self.assertEqual(self.board.board[6][1].type, Cell.CellType.RED)
        self.board.move(6, 1, 5, 0)
        self.assertEqual(self.board.board[5][0].type, Cell.CellType.RED)
        self.assertTrue(self.board.board[5][0].is_kinged())
        self.assertEqual(self.board.board[6][1].type, Cell.CellType.RED)
        self.assertFalse(self.board.board[6][1].is_kinged())

    def test_CannotMoveToEnemySpaceIfNoJump(self):
        self.board.move(5, 0, 4, 1)
        self.board.move(4, 1, 3, 2)
        self.assertEqual(self.board.board[3][2].type, Cell.CellType.RED)
        self.board.move(3, 2, 2, 1)
        self.assertEqual(self.board.board[3][2].type, Cell.CellType.RED)
        self.assertEqual(self.board.board[2][1].type, Cell.CellType.BLACK)

    def test_CanJumpEnemySpace(self):
        self.board.move(2, 1, 3, 2)
        self.board.move(3, 2, 4, 1)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.BLACK)
        self.board.move(5, 0, 3, 2)
        self.assertEqual(self.board.board[3][2].type, Cell.CellType.RED)
        self.assertEqual(self.board.board[4][1].type, Cell.CellType.EMPTY)

    def test_CannotMakeNonJumpIfJumpIsAvailable(self):
        pass


if __name__ == "__main__":
    ut.main()