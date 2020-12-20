from cell import Cell


class Board:
    def __init__(self):
        self.dim = 8  # while it may be possible to change this value, it's not recommended
        self._build_board()

    def show(self):
        """Prints a textual representation of the board"""
        for row in self.board:
            print("|", end='')
            for cell in row:
                print("[" + str(cell) + "]", end='')
            print("|")
        print()

    def get_cell(self, row, col):
        """Returns a specified cell"""
        return self.board[row][col]

    def move(self, row, col, new_row, new_col):
        """Swaps two specified cells, unless that move is considered invalid"""
        if self.is_valid_move(row, col, new_row, new_col):
            from_cell = self.get_cell(row, col)
            to_cell = self.get_cell(new_row, new_col)
            self.board[row][col], self.board[new_row][new_col] = to_cell, from_cell

        else:
            print("Invalid move!")

    def is_valid_move(self, row, col, new_row, new_col):
        """Checks the validity of a move"""
        return True

    def _build_board(self):
        """Builds a dim X dim board and fills it with cells, initializing them to the appropriate color"""
        self.board = []
        for row in range(self.dim):
            self.board.append([])
            for col in range(self.dim):
                if 3 <= row <= 4 or (row + col) % 2 == 0:
                    self.board[row].append(Cell(Cell.CellType.EMPTY))
                elif row < 3:
                    self.board[row].append(Cell(Cell.CellType.BLACK))
                else:
                    self.board[row].append(Cell(Cell.CellType.RED))


if __name__ == "__main__":
    board = Board()
    board.show()
    board.move(5, 0, 4, 1)
    board.show()
