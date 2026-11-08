"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 19, 2026
"""

def is_empty(board):
    for row in board: #board gives int of edge dimention
        for square in row:
            if square != " ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if y_end == 7 and d_y == 1: 
        end = "full"    
    elif x_end == len(board) - 1 and d_x == 1:
        end = "full"
    elif x_end == 0 and d_x == -1:
        end = "full"
    elif board[y_end + d_y][x_end + d_x] == " ":
        end = "empty"
    else:
        end = "full"
        
    y_start = y_end - (length*d_y) + d_y
    x_start = x_end - (length*d_x) + d_x
    
    if y_start <= 0 and d_y == 1:
        start = "full"
    elif x_start <= 0 and d_x == 1:
        start = "full"
    elif x_start == len(board[0]) - 1 and d_x == -1:
        start = "full"        
    elif board[y_start - d_y][x_start - d_x] == " ":
        start = "empty"
    else: 
        start = "full"
    
    if end == "empty" and start == "empty":
        return "OPEN"
    elif end == "empty" or start == "empty":
        return "SEMIOPEN"
    else:
        return "CLOSED"
        

    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    y = y_start
    x = x_start
    open_seq_count = 0
    semi_open_seq_count = 0
    seq_len = 0
    row = []
    
    #create row
    for i in range(len(board)):
        if i >= y_start:
            row.append(board[i][x])
            x += d_x
            
    for square in row:
        if square == col:
            seq_len += 1
            
            # check complete seq;
            if 0 <= y + d_y < len(board) and 0 <= x + d_x < len(board[0]):
                end = board[y + d_y][x + d_x]
            else:
                end = " "
                
            if 0 <= y - length*d_y < len(board) and 0 <= x - length*d_x < len(board[0]):
                start = board[y - length*d_y][x - length*d_x]
            else:
                start = " "
        else:
            seq_len = 0
            
        
        if seq_len == length and end != col and start != col: #as above, I don't understand the mix of +/- I think I was thinking going down means y decreases but you're right, x, y should be both + or both -
            if is_bounded(board, x, y, length, d_y, d_x) == "OPEN": 
                open_seq_count += 1
            elif is_bounded(board, x, y, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
        
        x += d_x
        y += d_y #+/-? fixed
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    
    y = 0
    for x in range(len(board)):
        result = detect_row(board, col, y, x, length, 1, 0) # 0, 1 --> 1, 0 (I think the previous one checks the same row each time each time? Because it starts in row y = 0, and only changed the x vaules thus staying in row 1, so I made it check all columns instead) good catch!
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
        
        result = detect_row(board, col, y, x, length, 1, 1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
    
    y = 7
    for x in range(len(board)):
        result = detect_row(board, col, y, x, length, 1, -1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
    
    
    x = 0
    for y in range(len(board)):
        result = detect_row(board, col, y, x, length, 0, 1)
        open_seq_count += result[0] # 1, 0 --> 0, 1
        semi_open_seq_count += result[1] # 1, 0 --> 0, 1
        
        result = detect_row(board, col, y, x, length, 1, 1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
        
        result = detect_row(board, col, y, x, length, 1, -1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
        
        # just created the result variable for the other cases to avoid calling detect_row twice for the same output


    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    best_score = 0
    new_score = 0
    for y in range(len(board)):
        for x in range(len(board[0])): # len(board) - > len(board[0])x corresponds to number of elements in each row, just to be safe in case number of row != number of col
            if board[y][x] == ' ': 
                board[y][x] = 'b'
                new_score = score(board)
                if new_score >= best_score:
                    best_score = new_score
                    move_y = y
                    move_x = x
                board[y][x] = ' '

    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])
    
def is_win(board):
    # check for closed 5 in a row
    is_closed_5 = False
    possible_d = [(1,0), (0,1), (1,1), (1,-1)]
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if x >= 4:
                for d in possible_d:
                    if is_bounded(board, y, x, 5, d[0], d[1]) == "CLOSED":
                        if board[y][x] == "b":
                            return ("Black won")
                        elif board[y][x] == "w":
                            return ("White won")
                
            
    
    if detect_rows(board, 'w', 5)[0] >= 1 or detect_rows(board, 'w', 5)[1] >= 1: # added condition to check index 1, as long as you have 5 in a row, it doesn't matter if its semi open or open, it can even be closed; but also it shouldn't be possible to have more than one 5 in a row at the same time, is checking = sufficient
        return("White won")
    if detect_rows(board, 'b', 5)[0] >= 1 or detect_rows(board, 'b', 5)[1] >= 1: #^
        return("Black won") # "White won" -> "Black won"
    for y in range(len(board)):
        for x in range(len(board[0])): #len(board) - > len(board[0])
            if board[y][x] == ' ':
                return "Continue playing"
    return "Draw"
    
def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_is_bounded2():
    board = make_empty_board(8)
    x = 3; y = 4; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 7
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded2 PASSED")
    else:
        print("TEST CASE for is_bounded2 FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0): 
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_row2():
    board = make_empty_board(8)
    x = 3; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, 2,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

if __name__ == '__main__':
    
    test_is_bounded2()
    test_detect_row2()
    '''
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()
    some_tests()
    board = make_empty_board(8)
    print_board(board)
    put_seq_on_board(board, 0, 0, 0, 1, 4, "b")
    print_board(board)
    print(detect_row(board, "b", 0, 0, 4, 0, 1))
    
    board = make_empty_board(8)
    put_seq_on_board(board, 3, 3, 1, -1, 2, "b")
    print_board(board)
    print(detect_row(board, "b", 0, 6, 2, 1,-1))
    print(detect_rows(board, "b", 2))
    '''
    
    #play_gomoku(8)
