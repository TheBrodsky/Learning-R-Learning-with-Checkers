from cell import Cell


class Board:
    def __init__(self):
        self.dim = 8
        self._build_board()

    def show(self):
        for row in self.board:
            print("|", end='')
            for cell in row:
                print("[" + str(cell) + "]", end='')
            print("|")

    def _build_board(self):
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
