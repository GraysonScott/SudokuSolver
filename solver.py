# Grayson Scott
# Solver for Sudoku using Backtracking Algorithm
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if (board[row][column] == 0):
                return (row, column)
    return None

def validate_row(board, row, number):
    for i in range(len(board[0])):
        if board[row][i] == number:
            return False
    return True

def validate_column(board, column, number):
    for i in range(len(board)):
        if board[i][column] == number:
            return False
    return True

# Takes the box as the row and column of the first square of the box
def validate_box(board, box_row, box_col, number):
    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_col * 3, box_col*3 + 3):
            if board[i][j] == number:
                return False
    return True

def validate_location(board, row, column, number):
    if validate_row(board, row, number) and validate_column(board, column, number) and validate_box(board, row // 3, column // 3, number):
        return True
    return False

def solve(board):
    current = find_empty(board)
    if not current:
        return True
    else:
        row, column = current
    for num in range(1, 10):
        if(validate_location(board, row, column, num)):
            board[row][column]=num
            if solve(board):
                return True
            board[row][column] = 0
    return False

print_board(board)
solve(board)
print("___________________")
print_board(board)