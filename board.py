from cell import Cell


class Board:
    def __init__(self):
        self.dim = 8  # while it may be possible to change this value, it's not recommended
        self.board = []
        self._build_board()

    def show(self) -> None:
        """Prints a textual representation of the board"""
        for row in self.board:
            print("|", end='')
            for cell in row:
                print("[" + str(cell) + "]", end='')
            print("|")
        print()

    def get_cell(self, row: int, col: int) -> Cell:
        """Returns a specified cell"""
        return self.board[row][col]

    def king_cell(self, row: int, col: int) -> None:
        """Kings the cell at the given coords"""
        cell = self.get_cell(row, col)
        if cell.type == Cell.CellType.EMPTY:
            print("Invalid cell to king!")
        else:
            cell.king()

    def move(self, row: int, col: int, new_row: int, new_col: int) -> None:
        """Swaps two specified cells, unless that move is a jump or is invalid"""
        if self._is_valid_move(row, col, new_row, new_col):
            from_cell = self.get_cell(row, col)
            to_cell = self.get_cell(new_row, new_col)

            if to_cell.type == Cell.CellType.EMPTY:  # moving to empty space, just swap
                self.board[row][col], self.board[new_row][new_col] = to_cell, from_cell
            else:  # jumping enemy piece
                pass

        else:
            print("Invalid move!")

    # =================
    # Private Functions
    # =================
    def _is_valid_move(self, row: int, col: int, new_row: int, new_col: int) -> bool:
        """Checks the validity of a move"""
        return (new_row, new_col) in self._get_valid_moves(row, col)

    def _get_valid_moves(self, row: int, col: int) -> set:
        """Returns a set containing coords of available moves for a given cell. Empty set if cell is empty"""
        cell = self.get_cell(row, col)
        passive_moves = set()  # moves to empty spaces. Can only be made if no offensive moves are available
        offensive_moves = set()  # moves which jump an enemy piece
        if cell.type == Cell.CellType.EMPTY:
            # empty cells can't move
            return set()
        else:
            for diag_coord in self._get_diagonal_cells(row, col):
                # Filters out negatively indexed moves (they're outside the board)
                if diag_coord[0] < 0 or diag_coord[1] < 0:
                    continue

                # Filters out backwards movement for unkinged pieces
                if not cell.is_kinged() and self._is_backward_movement(cell, row, diag_coord[0]):
                    continue

                # Filters out moves related to occupied spaces
                target_cell = self.get_cell(*diag_coord)
                if target_cell.type == Cell.CellType.EMPTY:  # empty cells can be moved into at this point
                    passive_moves.add(diag_coord)  # VALID MOVE: space is empty
                    continue
                elif target_cell.type == cell.type:  # friendly pieces cannot be jumped
                    continue
                else:
                    # check if enemy space can be jumped
                    jump_row = (2 * diag_coord[0]) - row  # the row this piece would jump to
                    jump_col = (2 * diag_coord[1]) - col  # the col this piece would jump to
                    jump_cell = self.get_cell(jump_row, jump_col)
                    if jump_cell.type == Cell.CellType.EMPTY:
                        offensive_moves.add(diag_coord)  # VALID MOVE: enemy piece can be jumped

            # only return passive moves if there are no available offensive moves
            return offensive_moves if offensive_moves else passive_moves

    def _is_backward_movement(self, cell: Cell, row: int, new_row: int):
        """Returns a True is a given cell would be moving backwards to 'new_row', False otherwise"""
        return cell.type == Cell.CellType.RED and new_row > row or \
               cell.type == Cell.CellType.BLACK and new_row < row

    def _get_diagonal_cells(self, row: int, col: int) -> set:
        """Returns a set containing coords of diagonally adjacent cells given a cell"""
        coords = set()
        for i in [-1, 1]:
            for j in [-1, 1]:
                coords.add((row + i, col + j))
        return coords

    def _build_board(self) -> None:
        """Builds a dim X dim board and fills it with cells, initializing them to the appropriate color"""
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
