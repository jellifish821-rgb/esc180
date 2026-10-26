'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
import copy


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
# part A
def determine_coord(square_num):
    if square_num % 3 == 0:
        col = 2
    elif (square_num + 1)%3 == 0:
        col = 1
    else:
        col = 0
    
    row = ((square_num - 1) // 3)
    
    coord = [row,col]
    
    return coord
# part B
def put_in_board(board, mark, square_num):
    coord = determine_coord(square_num) #[x,y]
    board[coord[0]][coord[1]] = mark
    
    return board


    

# Q6
def get_free_squares(board):
    free_sqrs = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                free_sqrs.append([i,j])
    return free_sqrs
            
def make_random_move(board, mark):
    possible_spaces = get_free_squares(board)
    move = possible_spaces[random.randint(0, len(get_free_squares(board))-1)]
    board[move[0]][move[1]] = mark
    return board
    

def is_row_all_marks(board, row_i, mark):
    for elem in board[row_i]:
        if elem != mark:
            return False
    return True

def is_col_all_marks(board, col_i, mark):
    for row in board:
        if row[col_i] != mark:
            return False
    return True

def is_diag(board, mark):
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    elif board[2][0] == mark and board[1][1] == mark and board[0][2] == mark:
        return True
    else:
        return False

def is_win(board, mark):
        for i in range(0,2):
            if is_row_all_marks(board, i, mark) == True or is_col_all_marks(board, i, mark) == True or is_diag(board, mark) == True:
                return True
        
def try_to_win(board, mark):
    possible_spaces = get_free_squares(board)
    prev_board = copy.deepcopy(board)
    mock_board = copy.deepcopy(board)
    for move in possible_spaces: # for each space avaliable, try to place a mark
        mock_board[move[0]][move[1]] = mark
        if is_win(mock_board, mark) == True:
            return mock_board
        else:
            mock_board = copy.deepcopy(prev_board)
    prev_board = make_random_move(board, mark)
    return prev_board
        
    

if __name__ == '__main__':
   
    board = make_empty_board()
    mark = "X"
    while True:
        move = int(input("Enter your move: "))
        if 1 <= move <=9:
            board = put_in_board(board, mark, move)
        
        print_board_and_legend(board)
        if is_win(board, mark) == True:
            print(f"{mark} wins!")
            break
        
        if mark == "X":
            mark = "O"
        elif mark == "O":
            mark = "X"
        
        board = try_to_win(board, mark)
        print_board_and_legend(board)
        if is_win(board, mark) == True:
            print(f"{mark} wins!")
            break
        
        if mark == "X":
            mark = "O"
        elif mark == "O":
            mark = "X"




            
        
'''
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)            
    '''