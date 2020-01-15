def solve(board):
    """
    takes in a grid and solves a Sudoku board using backtracking
    :param board: 2d list of ints
    :return: solution, a 2d list of ints, or original board if no solution available
    """
    row, col = find_empty(board)  # step 1. Find next empty cell to solve
    if row is not None and col is not None:  # exit at end of board
        for n in range(1, 10):  # step 2. try numbers 1-9
            if is_valid(board, n, row, col):  # step 2a. check row, col, and box for validity
                board[row][col] = n  # step 3. If valid enter value
                if solve(board):  # step 4. recurse and solve new board
                    return True
                board[row][col] = 0  # step 5. If we get to a board state that is not valid, backtrack
        return False  # no valid number found
    return True  # end of the board returns true to stop backtracking and exit recursion


def find_empty(board):
    """
    find the next position of a '0' in the board and returns the position
    :param board: 2d list of ints
    :return: int, int - row and column
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None, None


def is_valid(board, n, i, j):
    """
    Checks if given number, n, is valid in specific location(i, j)
    :param board: 2d list of ints
    :param n: int
    :param i: int, row of cell being checked
    :param j: int, col of cell being checked
    :return: boolean
    """
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
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if board[row][col] == n:
                return False
    return True


# Test Cases
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board2 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]

solve(board)
solve(board2)
for row in board:
    print(row)
print()
for row in board2:
    print(row)
