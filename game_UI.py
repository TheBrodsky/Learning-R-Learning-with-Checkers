from game import Game
import pygame as pg


def draw_board(surface, dim: int) -> None:
    for row in range(dim):
        for col in range(dim):
            color = (0, 0, 0) if (row + col) % 2 == 1 else (255, 255, 255)
            pg.draw.rect(surface, color, (row * 100, col * 100, 100, 100,))


def draw_pieces(surface, game: Game) -> None:
    for rpiece in game.board.red_pieces:
        row, col = rpiece.get_coords()
        pg.draw.circle(surface, (255, 0, 0), ((col * 100) + 50, (row * 100) + 50), 50)

    for bpiece in game.board.black_pieces:
        row, col = bpiece.get_coords()
        pg.draw.circle(surface, (100, 100, 100), ((col * 100) + 50, (row * 100) + 50), 50)


def select_piece(col: int, row: int) -> (int, int):
    col = col // 100
    row = row // 100
    return row, col


if __name__ == "__main__":
    pg.init()

    game = Game()
    game.random_turn()
    dim = game.board.dim
    screen = pg.display.set_mode([dim*100, dim*100])

    running = True
    from_cell = None
    to_cell = None

    while not game.is_game_finished() and running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if from_cell is None:
                    from_cell = select_piece(*pg.mouse.get_pos())
                elif to_cell is None:
                    to_cell = select_piece(*pg.mouse.get_pos())
                    game.do_turn(*from_cell, *to_cell)
                    from_cell = None
                    to_cell = None

        screen.fill((255, 255, 255))

        draw_board(screen, dim)
        if from_cell is not None:
            pg.draw.rect(screen, (237, 235, 128), (from_cell[1] * 100, from_cell[0] * 100, 100, 100,))
        draw_pieces(screen, game)

        pg.display.flip()

    pg.quit()
