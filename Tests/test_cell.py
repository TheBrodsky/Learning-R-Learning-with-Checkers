import unittest as ut
from Environment.cell import Cell


class CellTests(ut.TestCase):
    def setUp(self):
        self.cell = Cell(Cell.CellType.EMPTY, 0, 0)

    def test_CellInitializesToCorrectType(self):
        self.assertEqual(self.cell.type, Cell.CellType.EMPTY)
        self.cell = Cell(Cell.CellType.BLACK, 0, 0)
        self.assertEqual(self.cell.type, Cell.CellType.BLACK)
        self.cell = Cell(Cell.CellType.RED, 0, 0)
        self.assertEqual(self.cell.type, Cell.CellType.RED)

    def test_CellCanChangeType(self):
        self.cell.set_type(Cell.CellType.RED)
        self.assertEqual(self.cell.type, Cell.CellType.RED)
        self.cell.set_type(Cell.CellType.BLACK)
        self.assertEqual(self.cell.type, Cell.CellType.BLACK)
        self.cell.set_type(Cell.CellType.EMPTY)
        self.assertEqual(self.cell.type, Cell.CellType.EMPTY)

    def test_IsKinged(self):
        self.assertFalse(self.cell.is_kinged())
        self.cell.king()
        self.assertTrue(self.cell.is_kinged())


if __name__ == "__main__":
    ut.main()