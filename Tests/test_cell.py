import unittest as ut
from cell import Cell


class CellTests(ut.TestCase):
    def setUp(self):
        self.cell = Cell(Cell.CellType.EMPTY)

    def test_CellInitializesToCorrectType(self):
        self.assertEqual(self.cell.type, Cell.CellType.EMPTY)
        self.cell = Cell(Cell.CellType.BLACK)
        self.assertEqual(self.cell.type, Cell.CellType.BLACK)
        self.cell = Cell(Cell.CellType.RED)
        self.assertEqual(self.cell.type, Cell.CellType.RED)

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

    def test_IsKinged(self):
        self.assertFalse(self.cell.is_kinged())
        self.cell.king()
        self.assertTrue(self.cell.is_kinged())

if __name__ == "__main__":
    ut.main()