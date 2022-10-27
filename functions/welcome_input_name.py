def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
#########################################################################
def user_1_name_input():

    player_1=input("player 1 enter your name: ")
    player_1_list = [player_1,'X']

    return player_1_list
#########################################################################
def user_2_name_input():
    player_2=input("player 2 enter your name: ")
    player_2_list = [player_2,'O']

    return player_2_list
#########################################################################
prRed("Welcome to our tic Tac Toe 3D game")
print()
player_1_list = user_1_name_input()
player_2_list = user_2_name_input()