def solve(board):
    """
    takes in a grid and solves a Sudoku board using backtracking
    :param board: 2d list of ints
    :return: solution, a 2d list of ints
    """
    """
    steps to solve
    1. find next 'empty' space to solve
    2. try numbers 1-9 and see if any are valid
        a. check row, col, and box for validity
    3. if valid enter number and solve new board
    4. if no numbers are valid backtrack to last valid board and try again
    """
    i, j = find_empty(board)
    if i is not None and j is not None:
        for n in range(1, 10):
            if is_valid(board, n, i, j):
                board[i][j] = n
                solve(board)

    return board


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None, None


def is_valid(board, n, i, j):
    # check row
    for col in board[i]:
        if col == n:
            return False
    # check col
    for row in range(len(board)):
        if board[row][j] == n:
            return False
    # check box
    box_row = i // 3  # gives first row of box
    box_col = j // 3  # give first col of box
    # print(i, box_row, j, box_col)
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if board[row][col] == n:
                return False
    return True


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solved = solve(board)
for row in solved:
    print(row)
