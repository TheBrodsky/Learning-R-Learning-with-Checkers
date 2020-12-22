from game import Game
import pygame as pg


def draw_board(surface: pg.Display, dim: int) -> None:
    for row in range(dim):
        for col in range(dim):
            color = (0, 0, 0) if (row + col) % 2 == 1 else (255, 255, 255)
            pg.draw.rect(surface, color, (row * 100, col * 100, 100, 100,))


def draw_pieces(surface: pg.Display, game: Game) -> None:
    for rpiece in game.board.red_pieces:
        row, col = rpiece.get_coords()
        pg.draw.circle(surface, (0, 255, 0), ((row * 100) + 50, (col * 100) + 50), 50)


def select_piece(col: int, row: int) -> None:
    col = col // 100
    row = row // 100
    print(row, col)


if __name__ == "__main__":
    pg.init()

    game = Game()
    dim = game.board.dim
    screen = pg.display.set_mode([dim*100, dim*100])

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                select_piece(*pg.mouse.get_pos())

        screen.fill((255, 255, 255))

        draw_board(screen, dim)

        pg.display.flip()

    pg.quit()
