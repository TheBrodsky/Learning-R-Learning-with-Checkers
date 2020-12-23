import unittest as ut
from Environment.game import Game
from Environment.cell import Cell


class GameTests(ut.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = self.game.board
        self.game.set_turn(Cell.CellType.RED)

    def test_CannotMoveMoreThanOneSpaceUnlessJump(self):
        self.game.move(5, 0, 3, 2)
        self.assertEqual(self.board.get_cell(5, 0).type, Cell.CellType.RED)
        self.assertEqual(self.board.get_cell(3, 2).type, Cell.CellType.EMPTY)

    def test_CannotMoveToOutsideBoard(self):
        self.game.move(5, 0, 4, -1)
        self.assertEqual(self.board.get_cell(5, 0).type, Cell.CellType.RED)
        self.game.move(6, 7, 5, 8)
        self.assertEqual(self.board.get_cell(6, 7).type, Cell.CellType.RED)

    def test_CannotMoveBackwardIfNotKinged(self):
        self.game.move(5, 0, 4, 1)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.RED)
        self.game.set_turn(Cell.CellType.RED)
        self.game.move(4, 1, 5, 0)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.RED)
        self.assertEqual(self.board.get_cell(5, 0).type, Cell.CellType.EMPTY)

    def test_CanMoveBackwardIfKinged(self):
        self.game.move(5, 0, 4, 1)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.RED)
        self.board.get_cell(4, 1).king()
        self.game.set_turn(Cell.CellType.RED)
        self.game.move(4, 1, 5, 0)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.EMPTY)
        self.assertEqual(self.board.get_cell(5, 0).type, Cell.CellType.RED)

    def test_CannotMoveToFriendlySpace(self):
        cell1 = self.board.get_cell(6, 1)
        cell2 = self.board.get_cell(5, 0)
        self.game.move(6, 1, 5, 0)
        self.assertEqual(cell1, self.board.get_cell(6, 1))
        self.assertEqual(cell2, self.board.get_cell(5, 0))

    def test_CannotMoveToEnemySpaceIfNoJump(self):
        self.game.do_turn(5, 0, 4, 1)
        self.game.do_turn(2, 1, 3, 2)
        self.game.do_turn(4, 1, 3, 2)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.RED)
        self.assertEqual(self.board.get_cell(3,2).type, Cell.CellType.BLACK)

    def test_CanJumpEnemySpace(self):
        self.game.do_turn(5, 0, 4, 1)
        self.game.do_turn(2, 1, 3, 2)
        self.game.set_turn(Cell.CellType.BLACK)
        self.game.do_turn(3, 2, 4, 1)
        self.assertEqual(self.board.get_cell(5, 0).type, Cell.CellType.BLACK)
        self.assertEqual(self.board.get_cell(4, 1).type, Cell.CellType.EMPTY)
        self.assertEqual(len(self.board.red_pieces), 11)
        self.assertEqual(len(self.board.black_pieces), 12)

    def test_CannotMakeNonJumpIfJumpIsAvailable(self):
        self.game.do_turn(5, 0, 4, 1)
        self.game.do_turn(2, 1, 3, 2)
        self.game.set_turn(Cell.CellType.BLACK)
        self.game.do_turn(2, 7, 3, 6)
        self.assertEqual(self.board.get_cell(2, 7).type, Cell.CellType.BLACK)
        self.assertEqual(self.board.get_cell(3, 6).type, Cell.CellType.EMPTY)


if __name__ == "__main__":
    ut.main()