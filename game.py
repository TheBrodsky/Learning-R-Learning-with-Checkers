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

    def jump_chain(self, row: int, col: int, jumps: set):
        """Handles instances where multiple jumps happen in a row"""
        can_jump = True
        while can_jump:
            try:
                self.board.show()
                newrow, newcol = input(f"Subsequent jump available. Choose which piece to take: {str(jumps)}").split()
                newrow, newcol = int(newrow), int(newcol)
                if (newrow, newcol) in jumps:
                    can_jump, coords, jumps = self.board.move(row, col, newrow, newcol)
                    row, col = coords
                else:
                    print("Invalid move: Selected cell not available to take")
            except ValueError:
                print("Invalid move: Syntax incorrect, please input move as 'row, col'")

    def check_king(self, cell: Cell) -> None:
        """Checks if a given cell should be kinged"""
        if cell.type == Cell.CellType.RED:
            if cell.get_coords()[0] == 0:
                cell.king()
        else:
            if cell.get_coords()[0] == self.board.dim:
                cell.king()

    def game_loop(self, starting_color: Cell.CellType) -> None:
        """The core game loop. Once called, runs until the current game ends."""
        self.cur_turn = starting_color
        self.cur_moves = self.board.get_all_valid_moves(self.cur_turn)

        while not self.is_game_finished():
            turn_str = "RED" if self.cur_turn == Cell.CellType.RED else "BLACK"
            try:
                print(self.cur_moves)
                self.board.show()
                row, col, newrow, newcol = input(f"{turn_str}'s turn: ").split()
                if self.move(int(row), int(col), int(newrow), int(newcol)):
                    # a valid move was given, change turns
                    self.step()
                    continue
                else:
                    # an invalid move was given, repeat turn
                    continue

            except ValueError:
                print("Invalid move: Syntax incorrect, please input move as 'row, col, new_row, new_col'")

    def do_turn(self, row: int, col: int, new_row: int, new_col: int) -> None:
        """Like game_loop but only a single loop. Used for the UI, which needs to step through turn by turn."""
        if self.move(row, col, new_row, new_col):
            self.step()

    def is_game_finished(self):
        return len(self.board.red_pieces) == 0 or len(self.board.black_pieces) == 0
