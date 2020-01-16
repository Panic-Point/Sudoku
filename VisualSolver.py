from typing import Optional

import pygame

pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


class Cell:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw_cell(self, screen):
        fnt = pygame.font.SysFont("comicsans", 40)
        offset = self.width
        x = self.col * offset
        y = self.row * offset

        # draw new white cell
        pygame.draw.rect(screen, WHITE, (x, y, offset, offset), 0)

        # draw new number
        text = fnt.render(str(self.value), 1, BLACK)
        screen.blit(text, (x + offset / 2, y + offset / 2))


class Board:
    def __init__(self, board, width, height):
        self.rows = len(board[0])
        self.cols = len(board)
        self.cells = [Cell(board[i][j], i, j, width // self.rows, height // self.cols) for j in range(self.cols) for i
                      in range(self.rows)]
        self.model = board[:]


def draw_grid(board, screen):
    w, h = pygame.display.get_surface().get_size()
    offset = h // 9
    for row in range(board.rows):
        if row % 3 == 0:
            margin = 5
        else:
            margin = 2
        pygame.draw.line(screen, BLACK, (0, row * offset), (w, row * offset), margin)
    for col in range(board.cols):
        if col % 3 == 0:
            margin = 5
        else:
            margin = 2
        pygame.draw.line(screen, BLACK, (col * offset, 0), (col * offset, h), margin)


def vis_solver(board, screen, speed):
    cell = find_empty(board)
    if speed == 'S':
        delay = 100
    elif speed == 'M':
        delay = 50
    else:
        delay = 10
    if cell is not None:
        for n in range(1, 10):
            if is_valid(board.model, n, cell.row, cell.col):
                cell.value = n
                board.model[cell.row][cell.col] = n
                cell.draw_cell(screen)
                draw_grid(board, screen)
                pygame.display.update()
                pygame.time.delay(delay)
                if vis_solver(board, screen, speed):
                    return True
                cell.value = 0
                board.model[cell.row][cell.col] = 0
                cell.draw_cell(screen)
                pygame.display.update()
                draw_grid(board, screen)
                pygame.time.delay(delay)
        return False
    return True


def find_empty(board: Board) -> Optional[Cell]:
    for i in range(board.rows):
        for j in range(board.cols):
            if board.model[i][j] == 0:
                for cell in board.cells:
                    if cell.row == i and cell.col == j:
                        return cell
    return None


def is_valid(model, n, i, j):
    # check row
    for col in model[i]:
        if col == n:
            return False
    # check col
    for row in range(len(model)):
        if model[row][j] == n:
            return False
    # check box
    box_row = i // 3  # gives first row of box
    box_col = j // 3  # give first col of box
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if model[row][col] == n:
                return False
    return True


def main(board, speed):
    WINDOW_SIZE = [540, 540]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(WHITE)
    for c in board.cells:
        c.draw_cell(screen)
    draw_grid(board, screen)
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vis_solver(board, screen, speed)


# board0 takes A REALLY long time visually to solve. It isn't an infinite loop I promise
board0 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board1 = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

b = Board(board0, 540, 540)
speed = 'F'  # F = 10ms delay, M = 50ms delay, S = 100ms delay
main(b, speed)

pygame.quit()
