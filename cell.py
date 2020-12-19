from enum import Enum


class Cell:
    class CellType(Enum):
        EMPTY = 0
        RED = 1
        BLACK = 2

    def __init__(self):
        self.type = self.CellType.EMPTY

    def set_type(self, new_type: CellType):
        self.type = new_type

    def __str__(self):
        if self.type == self.CellType.EMPTY:
            return " "
        elif self.type == self.CellType.RED:
            return "R"
        else:
            return "B"
