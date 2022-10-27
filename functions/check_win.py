
#################### COL 2 D ###############################
def is_win_in_col_2D(board: dict) -> bool:
    outer_i = 1
    while outer_i < len(board):  # outer_i will run from 1 to 27

        inner_i = outer_i
        curr_board_limit = outer_i + 3
        while inner_i < curr_board_limit:  # will run 3 times for each board to check column win
            if board[inner_i] == board[inner_i + 3] == board[inner_i + 6]:
                return True
            inner_i += 1

        inner_i -= 1
        outer_i = inner_i
        outer_i += 7  # increment index to next level

    return False  # no winner was found

##################### COL 3D ###############################
def is_win_in_col_3D(board: dict) -> bool:
    for i in range(1, 10):
        if board[i] == board[i + 9] == board[i + 18]:
            return True

    return False  # no winner was found

##################### ROW 2D ###############################

def is_win_in_row_2D(board: dict) -> bool:
    outer_i = 1
    while outer_i <= len(board):  # outer_i will run from 1 to 27

        inner_i = outer_i
        curr_board_limit = outer_i + 1
        while inner_i < curr_board_limit:  # will run 3 times for each board to check column win
            if board[inner_i] == board[inner_i + 1] == board[inner_i + 2]:
                return True
            inner_i += 1

        inner_i -= 1
        outer_i = inner_i
        outer_i += 3  # increment index to next level

    return False  # no winner was found

##################### diagonal 2D RIGHT TO LEFT ###############################
#
def is_win_in_diagonal_right_to_left_2D(board: dict) -> bool:
    outer_i = 1
    while outer_i < len(board):  # outer_i will run from 1 to 27

        inner_i = outer_i
        curr_board_limit = outer_i + 27
        while inner_i < curr_board_limit:  # will run 3 times for each board to check column win
            if board[inner_i] == board[inner_i + 4] == board[inner_i + 8]:
                return True
            inner_i += 9

        inner_i -= 1
        outer_i = inner_i
        outer_i += 7  # increment index to next level

    return False  # no winner was found

##################### diagonal 2D LEFT TO RIGHT ###############################
#
def is_win_in_diagonal_left_to_right_2D(board: dict) -> bool:
    outer_i = 3
    while outer_i < len(board):  # outer_i will run from 1 to 27

        inner_i = outer_i
        curr_board_limit = outer_i + 27
        while inner_i < curr_board_limit:  # will run 3 times for each board to check column win
            if board[inner_i] == board[inner_i + 2] == board[inner_i + 4]:
                return True
            inner_i += 9

        inner_i -= 1
        outer_i = inner_i
        outer_i += 7  # increment index to next level

    return False  # no winner was found

##################### diagonal 3D ###############################

def is_win_in_diagonal_3D(board: dict) -> bool:
    if board[1] == board[13] == board[25]:
        return True
    elif board[2] == board[14] == board[26]:
        return True
    elif board[3] == board[15] == board[27]:
        return True
    elif board[7] == board[13] == board[19]:
        return True
    elif board[8] == board[14] == board[20]:
        return True
    elif board[9] == board[15] == board[21]:
        return True
    elif board[1] == board[11] == board[21]:
        return True
    elif board[4] == board[14] == board[24]:
        return True
    elif board[7] == board[17] == board[27]:
        return True
    elif board[3] == board[11] == board[19]:
        return True
    elif board[6] == board[14] == board[22]:
        return True
    elif board[9] == board[17] == board[25]:
        return True
    elif board[1] == board[14] == board[27]:
        return True
    elif board[3] == board[14] == board[25]:
        return True
    elif board[9] == board[14] == board[19]:
        return True
    elif board[7] == board[14] == board[21]:
        return True

    return False  # no winner was found

##################### diagonal 3D ###############################

def is_game_over(board):
    ans = (is_win_in_col_2D(board) or
           is_win_in_col_3D(board) or
           is_win_in_row_2D(board) or
           is_win_in_diagonal_right_to_left_2D(board) or
           is_win_in_diagonal_left_to_right_2D(board) or
           is_win_in_diagonal_3D(board)
           )
    return ans
