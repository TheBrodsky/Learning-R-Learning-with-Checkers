import unittest as ut
from cell import Cell


class CellTests(ut.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_EmptyCellInitialization(self):
        self.assertEqual(self.cell.type, Cell.CellType.EMPTY)

    def test_CellCanChangeType(self):
        self.cell.set_type(Cell.CellType.RED)
        self.assertEqual(self.cell.type, Cell.CellType.RED)
        self.cell.set_type(Cell.CellType.BLACK)
        self.assertEqual(self.cell.type, Cell.CellType.BLACK)
        self.cell.set_type(Cell.CellType.EMPTY)
        self.assertEqual(self.cell.type, Cell.CellType.EMPTY)

    def test_CellToString(self):
        self.assertEqual(str(self.cell), " ")
        self.cell.set_type(Cell.CellType.RED)
        self.assertEqual(str(self.cell), "R")
        self.cell.set_type(Cell.CellType.BLACK)
        self.assertEqual(str(self.cell), "B")

if __name__ == "__main__":
    ut.main()