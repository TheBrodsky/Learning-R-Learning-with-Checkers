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
        row = []
        for col in range(self.dim):
            row.append(Cell())

        for r in range(self.dim):
            self.board.append(row)


if __name__ == "__main__":
    board = Board()
    board.show()
