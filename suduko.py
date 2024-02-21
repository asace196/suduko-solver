def solve_sudoku(board):
    if not find_empty_location(board):
        return True  # Puzzle solved successfully

    row, col = find_empty_location(board)

    for num in range(1, 10):  # Try numbers from 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If solution found, return True

            board[row][col] = 0  # Backtrack if the current configuration doesn't lead to a solution

    return False  # Trigger backtracking


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # Return row and column of an empty cell
    return None  # If no empty cell is found


def is_safe(board, row, col, num):
    # Check if the number is not present in the current row
    if num in board[row]:
        return False

    # Check if the number is not present in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True  # Number can be placed safely


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku before solving:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSudoku solved successfully:")
        print_board(board)
    else:
        print("\nNo solution exists for the given Sudoku.")
