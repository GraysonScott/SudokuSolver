# Grayson Scott
# Sudoku Generator using Backtracking Algorithm

from random import shuffle, randint

board = []
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

numberList = [1,2,3,4,5,6,7,8,9]

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
    print()

# Checks if the board is full
def check_full(board):
    for row in range(0, 9):
        for column in range(0, 9):
            if (board[row][column] == 0):
                return False
    return True

# Checks the row for duplicates
def validate_row(board, row, number):
    for i in range(0, 9):
        if board[row][i] == number:
            return False
    return True

# Checks the column for duplicates
def validate_column(board, column, number):
    for i in range(0, 9):
        if board[i][column] == number:
            return False
    return True

# Checks the box for duplicates
# Takes the box as the row and column of the first square of the box
def validate_box(board, box_row, box_col, number):
    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_col * 3, box_col*3 + 3):
            if board[i][j] == number:
                return False
    return True

# Helper function that checks each requirement
def validate_location(board, row, column, number):
    if validate_row(board, row, number) and validate_column(board, column, number) and validate_box(board, row // 3, column // 3, number):
        return True
    return False

# Solves the board, increases the count for each solution
def solve(board):
    global counter
    for i in range(0, 81):
        row = i // 9
        column = i % 9
        if board[row][column] == 0:
            for num in range(1, 10):
                if(validate_location(board, row, column, num)):
                    board[row][column]=num
                    if check_full(board):
                        counter += 1
                        break
                    else:
                        if solve(board):
                            return True
            break
    board[row][column] = 0

# Creates a random, valid, solved board
def fill_board(board):
    global counter
    for i in range(0, 81):
        row = i // 9
        column = i % 9
        if board[row][column] == 0:
            shuffle(numberList)
            for num in numberList:
                if(validate_location(board, row, column, num)):
                    board[row][column]=num
                    if check_full(board):
                        return True
                    else:
                        if fill_board(board):
                            return True
            break
    board[row][column] = 0

fill_board(board)

attempts = 5 
counter=1
while attempts>0:
  # Select a random cell that is not already empty
  row = randint(0,8)
  col = randint(0,8)
  while board[row][col]==0:
    row = randint(0,8)
    col = randint(0,8)
  # Remember its cell value in case we need to put it back  
  backup = board[row][col]
  board[row][col]=0
  
  #Take a full copy of the board
  board_copy = []
  for r in range(0,9):
     board_copy.append([])
     for c in range(0,9):
        board_copy[r].append(board[r][c])
  
  #Count the number of solutions that this board has (using a backtracking approach implemented in the solveboard() function)
  counter=0      
  solve(board_copy)   
  #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the board
  if counter!=1:
    board[row][col]=backup
    #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
    attempts -= 1

print_board(board)