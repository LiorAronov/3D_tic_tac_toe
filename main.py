from check_win import is_game_over
import random as rd
from color_fronot import prRed, prGreen, prPurple, prLightPurple, prCyan, prYellow, prLightGray, prorange, prCyan

##################################################################################################################################################

def get_player_names():
    prGreen('-' * 80)
    prGreen("                     ██████████████████████████████████████ ")
    prGreen("                     █ Welcome to our tic Tac Toe 3D game █ ")
    prGreen("                     █   by Gal, Lior, Hagai, and Yoav    █ ")
    prGreen("                     ██████████████████████████████████████ ")
    prGreen('-' * 80)
    print()
    name1 = input(" player 1 enter your name: ")
    print('-' * 80)
    name2 = input(" player 2 enter your name: ")
    print('-' * 80)
    names = [name1, name2]
    return names


##################################################################################################################################################


def print_board(board):
    prPurple("                             ___________________________")
    prPurple("                            /        /        /        /")
    prPurple(f"                           /    {board[1]:2}  /    {board[2]:2}  /    {board[3]:2}  /")
    prPurple("                          /________/________/________/")
    prPurple("                         /        /        /        /")
    prPurple(f"                        /   {board[4]:2}   /   {board[5]:2}   /     {board[6]:2} /")
    prPurple("                       /________/________/________/")
    prPurple("                      /        /        /        /")
    prPurple(f"                     /    {board[7]:2}  /    {board[8]:2}  /     {board[9]:2} /")
    prPurple("                    /________/________/________/")

    prGreen("                             ___________________________")
    prGreen("                            /        /        /        /")
    prGreen(f"                           /   {board[10]:2}   /    {board[11]:2}  /    {board[12]:2}  /")
    prGreen("                          /________/________/________/")
    prGreen("                         /        /        /        /")
    prGreen(f"                        /   {board[13]:2}   /   {board[14]:2}   /    {board[15]:2}  /")
    prGreen("                       /________/________/________/")
    prGreen("                      /        /        /        /")
    prGreen(f"                     /   {board[16]:2}   /   {board[17]:2}   /    {board[18]:2}  /")
    prGreen("                    /________/________/________/")

    prYellow("                             ___________________________")
    prYellow("                            /        /        /        /")
    prYellow(f"                           /   {board[19]:2}   /   {board[20]:2}   /    {board[21]:2}  /")
    prYellow("                          /________/________/________/")
    prYellow("                         /        /        /        /")
    prYellow(f"                        /   {board[22]:2}   /   {board[23]:2}   /    {board[24]:2}  /")
    prYellow("                       /________/________/________/")
    prYellow("                      /        /        /        /")
    prYellow(f"                     /   {board[25]:2}   /   {board[26]:2}   /    {board[27]:2}  /")
    prYellow("                    /________/________/________/")


##################################################################################################################################################
def get_random_starter():
    starter_index = rd.randint(0, 1)
    return starter_index


##################################################################################################################################################
def create_players(names: list[str], starter_index):
    players = []

    for i in range(2):
        curr_player = {"name": names[i].title(), "num_of_wins": 0}
        if i == starter_index:
            curr_player["sign"] = "X"
        else:
            curr_player["sign"] = "O"
        players.append(curr_player)

    return players


##################################################################################################################################################
def update_num_of_wins(players: list[dict], winner_index: int):
    players[winner_index]["num_of_wins"] += 1


##################################################################################################################################################
def make_move(board, players, turn_index):
    move = get_player_move(board, players, turn_index)
    board[int(move)] = players[turn_index]["sign"]


##################################################################################################################################################
def is_move_valid(board: list[dict], player_move: str):
    answer = False
    if player_move.isdigit():
        if player_move in board.values():  # check if move is possible in board
            answer = True
        else:
            prRed("     ______________________________________________________________________")
            prRed("    |                                                                      |")
            prRed("    | Invalid move, your move is out of range or cell is taken, try again. |")
            prRed("    |______________________________________________________________________|")
    else:
        prRed("                     ____________________________________")
        prRed("                    |                                    |")
        prRed("                    | Invalid input, insert numbers only.|")
        prRed("                    |____________________________________|")

    return answer


##################################################################################################################################################
def change_turn(turn_i):
    next_turn = turn_i + 1
    return next_turn % 2


##################################################################################################################################################
def get_player_move(board, players, turn_index) -> str:
    is_valid = False
    name = players[turn_index]['name']
    sign = players[turn_index]['sign']
    while not is_valid:
        print()
        player_move = input(f"{name}, choose a number from the board to put your {sign} in: ")
        is_valid = is_move_valid(board, player_move)

    return player_move


##################################################################################################################################################
def turn(board, players, turn_index):
    print_board(board)
    make_move(board, players, turn_index)
    is_finished = is_game_over(board)
    return is_finished


##################################################################################################################################################
def init():
    board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18',
             19: '19', 20: '20', 21: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27'}
    return board


##################################################################################################################################################
def is_answer_valid(answer):
    return answer == "y" or answer == "n"


##################################################################################################################################################
def is_repeat_game():
    valid = False
    counter = 0

    while valid == False and counter < 3:
        print()
        answer = input("Would you like to play another game? prass y or n: ")
        print()
        if (answer == 'y') or (answer == 'yes'):
            print()
            prGreen("                     ██████████████████████████████████████ ")
            prGreen("                     █████ Let\'s play another game!! ██████ ")
            prGreen("                     ██████████████████████████████████████ ")
            print()
            valid = True
            answer = True

        elif (answer == 'n') or (answer == 'no'):
            prGreen("-" * 80)
            print()
            prGreen('                        See you next time! Bye...')
            print()

            valid = True
            answer = False

        else:
            print("Invalid input")
            counter += 1

    return answer


#########################################################################
def check_draw(board):
    for val in board.values():
        if val.isdigit():
            return False
    return True


#########################################################################
def the_tic_tac_toe_3D_show():
    another_game = True
    names = get_player_names()
    turn_index = get_random_starter()
    players = create_players(names, turn_index)

    while another_game == True:
        board = init()
        is_finished = False

        turn_index = get_random_starter()
        is_draw = False
        while not is_finished:
            is_there_a_winner = turn(board, players, turn_index)
            is_draw = check_draw(board)
            # the game ends if there is a winner or draw
            is_finished = is_there_a_winner or is_draw
            if is_there_a_winner == True:
                update_num_of_wins(players, turn_index)
                print_board(board)
                print()
                prGreen('-' * 80)

                prGreen(
                    f"                     {players[turn_index]['name']} is the winner! with the sign {players[turn_index]['sign']}")
                prGreen('-' * 80)

            turn_index = change_turn(turn_index)

        another_game = is_repeat_game()

    prGreen("-" * 80)
    print()
    prGreen("                        Hope you enjoyed the game")
    print()
    prGreen(f"                            {players[0]['name']} is with {players[0]['num_of_wins']} wins")
    print()
    prGreen(f"                            {players[1]['name']} is with {players[1]['num_of_wins']} wins")
    print()
    prGreen("-" * 80)


the_tic_tac_toe_3D_show()
