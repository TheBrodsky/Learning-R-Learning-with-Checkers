from board import Board
from cell import Cell
from random import choice


class Game:
    def __init__(self):
        self.board = Board()
        self.cur_turn = None
        self.cur_moves = {}

    def random_turn(self) -> None:
        self.cur_turn = choice([Cell.CellType.RED, Cell.CellType.BLACK])
        self.cur_moves = self.board.get_all_valid_moves(self.cur_turn)

    def set_turn(self, color: Cell.CellType) -> None:
        self.cur_turn = color
        self.cur_moves = self.board.get_all_valid_moves(self.cur_turn)

    def step(self) -> None:
        """Changes turn and updates"""
        if self.cur_turn == Cell.CellType.RED:
            self.cur_turn = Cell.CellType.BLACK
        else:
            self.cur_turn = Cell.CellType.RED

        self.cur_moves = self.board.get_all_valid_moves(self.cur_turn)

    def move(self, row: int, col: int, new_row: int, new_col: int) -> bool:
        """Calls Board.move(), but enforces move validity. Returns True if turn should advance, False otherwise"""
        cell = self.board.get_cell(row, col)
        if cell.type == self.cur_turn:  # selected cell must contain the current player's piece
            try:
                if (new_row, new_col) in self.cur_moves[(row, col)]:
                    # move is valid, make move
                    can_jump, coords, jumps = self.board.move(row, col, new_row, new_col)
                    if can_jump:
                        self.cur_moves = {coords: jumps}  # cur_moves is the subsequent jump(s) and no other moves
                        self.check_king(cell)
                        return False
                    else:
                        self.check_king(cell)
                        return True

                else:
                    print("Invalid move: Selected piece cannot make that move")

            except KeyError:
                print("Invalid move: Selected piece cannot be moved")

        else:
            if cell.type == Cell.CellType.EMPTY:
                print("Invalid move: Selected empty cell")
            else:
                print("Invalid move: Cannot move opponent's piece")

        return False

    def check_king(self, cell: Cell) -> None:
        """Checks if a given cell should be kinged"""
        if cell.type == Cell.CellType.RED:
            if cell.get_coords()[0] == 0:
                cell.king()
        else:
            if cell.get_coords()[0] == self.board.dim - 1:
                cell.king()

    def do_turn(self, row: int, col: int, new_row: int, new_col: int) -> None:
        """Like game_loop but only a single loop. Used for the UI, which needs to step through turn by turn."""
        if self.move(row, col, new_row, new_col):
            self.step()

    def is_game_finished(self):
        return len(self.board.red_pieces) == 0 or len(self.board.black_pieces) == 0
