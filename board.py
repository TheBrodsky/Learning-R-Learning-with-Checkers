from cell import Cell


class Board:
    def __init__(self):
        self.dim = 8  # changing this may have unpredictable results and cause tests to fail
        self.board = []
        self.red_pieces = set()  # used for quick iteration over game pieces rather than over whole board
        self.black_pieces = set()
        self._build_board()

    def show(self) -> None:
        """Prints a textual representation of the board"""
        print(" " * 3, end='')
        for c in range(self.dim):
            print(f" {c} ", end='')
        print()

        for r, row in enumerate(self.board):
            print(f"{r} |", end='')
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

    def move(self, row: int, col: int, new_row: int, new_col: int) -> (bool, (int, int), set):
        """Swaps cells or jumps cell. Assumes move is valid. Returns 3 things:
        True or False is subsequent jump is available; row and col of moved piece; set of moves for moved piece"""
        from_cell = self.get_cell(row, col)
        to_cell = self.get_cell(new_row, new_col)

        if to_cell.type == Cell.CellType.EMPTY:  # moving to empty space, which is a normal move
            to_cell.set_coords(row, col)
            from_cell.set_coords(new_row, new_col)
            self.board[row][col], self.board[new_row][new_col] = to_cell, from_cell
            return False, (new_row, new_col), None

        else:  # 'moving' to nonempty space
            # Assumptions: space is occupied by enemy piece; enemy piece has empty space 'behind' it
            # These assumptions are not enforced by Board, but by Game

            # remove jumped piece from corresponding side
            if from_cell.type == Cell.CellType.RED:
                self.black_pieces.remove(to_cell)
            else:
                self.red_pieces.remove(to_cell)
            to_cell.set_type(Cell.CellType.EMPTY)  # set piece to empty space

            # get space being jumped to
            jump_row = (2 * new_row) - row  # row this piece would jump to
            jump_col = (2 * new_col) - col  # col this piece would jump to
            to_cell = self.get_cell(jump_row, jump_col)  # empty space being jumped to

            # swap spaces
            to_cell.set_coords(row, col)
            from_cell.set_coords(jump_row, jump_col)
            self.board[row][col], self.board[jump_row][jump_col] = to_cell, from_cell

            # check for subsequent jump
            can_jump, jumps = self._get_valid_moves(jump_row, jump_col)
            return can_jump, (jump_row, jump_col), jumps

    def get_all_valid_moves(self, color: Cell.CellType) -> {(int, int): set}:
        """Returns a dictionary of sets with all possible moves for a given player"""
        can_jump = False
        all_moves = {}
        pieces = self.red_pieces if color == Cell.CellType.RED else self.black_pieces
        for piece in pieces:
            jump, moves = self._get_valid_moves(*piece.get_coords())
            if not can_jump:
                if jump:
                    # at least 1 jump found; all non-jump moves must be removed and future moves must be jumps
                    can_jump = True  # ensure future moves are only jumps
                    all_moves = {piece.get_coords(): moves}  # remove non-jump moves; add newly-discovered jumps
                else:
                    # no jumps yet found; add all valid moves
                    all_moves[piece.get_coords()] = moves
            else:
                if jump:
                    # since can_jump is true, only jumps are added. Non-jumps are ignored
                    all_moves[piece.get_coords()] = moves

        return all_moves

    # =================
    # Private Functions
    # =================
    def _get_valid_moves(self, row: int, col: int) -> (bool, set):
        """Returns a set containing coords of available moves for a given cell. Empty set if cell is empty"""
        cell = self.get_cell(row, col)
        moves = set()  # moves to empty spaces. Can only be made if no offensive moves are available
        jumps = set()  # moves which jump an enemy piece
        if cell.type == Cell.CellType.EMPTY:
            # empty cells can't move
            return set()
        else:
            for diag_coord in self._get_diagonal_cells(row, col):
                # Filters out cells outside board
                if not 0 <= diag_coord[0] < self.dim or not 0 <= diag_coord[1] < self.dim:
                    continue

                # Filters out backwards movement for unkinged pieces
                if not cell.is_kinged() and self._is_backward_movement(cell, row, diag_coord[0]):
                    continue

                # Filters out moves related to occupied spaces
                target_cell = self.get_cell(*diag_coord)
                if target_cell.type == Cell.CellType.EMPTY:  # empty cells can be moved into at this point
                    moves.add(diag_coord)  # VALID MOVE: space is empty
                    continue
                elif target_cell.type == cell.type:  # friendly pieces cannot be jumped
                    continue
                else:
                    # check if enemy space can be jumped
                    jump_row = (2 * diag_coord[0]) - row  # the row this piece would jump to
                    jump_col = (2 * diag_coord[1]) - col  # the col this piece would jump to
                    if 0 <= jump_row < self.dim and 0 <= jump_col < self.dim:  # cell being jumped to is within board
                        jump_cell = self.get_cell(jump_row, jump_col)
                        if jump_cell.type == Cell.CellType.EMPTY:
                            jumps.add(diag_coord)  # VALID MOVE: enemy piece can be jumped

            # only return passive moves if there are no available offensive moves
            can_jump = bool(jumps)
            return can_jump, jumps if can_jump else moves

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
                if 3 <= row <= 4 or (row + col) % 2 == 0:  # middle rows are empty; every other square is empty
                    self.board[row].append(Cell(Cell.CellType.EMPTY, row, col))
                elif row < 3:
                    cell = Cell(Cell.CellType.BLACK, row, col)
                    self.board[row].append(cell)
                    self.black_pieces.add(cell)
                else:
                    cell = Cell(Cell.CellType.RED, row, col)
                    self.board[row].append(cell)
                    self.red_pieces.add(cell)