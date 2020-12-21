from enum import Enum


class Cell:
    class CellType(Enum):
        """Basic enum class used to distinguish game pieces"""
        EMPTY = 0
        RED = 1
        BLACK = 2

    def __init__(self, init_type: CellType, row: int, col: int):
        self.type = init_type
        self.row = row
        self.col = col
        self.kinged = False

    def get_coords(self) -> (int, int):
        return self.row, self.col

    def set_coords(self, row: int, col: int) -> None:
        """Changes the row and col of this cell"""
        self.row = row
        self.col = col

    def set_type(self, new_type: CellType) -> None:
        """Changes the CellType of this cell"""
        self.type = new_type

    def is_kinged(self):
        return self.kinged

    def king(self):
        self.kinged = True

    def __str__(self):
        if self.type == self.CellType.EMPTY:
            return " "
        elif self.type == self.CellType.RED:
            return "R"
        else:
            return "B"
