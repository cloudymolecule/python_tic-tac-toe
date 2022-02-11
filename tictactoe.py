import os

# welcome message
from curses.ascii import isdigit


def welcome():
    os.system('clear')
    print('Welcome to Tic Tac Toe!')
    print('')

# player selection
def player_select():
    players = {'p1': None, 'p2': None}
    while players['p1'] == None:
        print('')
        choice = input('Will Player One be "X" or "O"? ').upper()
        if choice == 'X':
            players = {'p1': 'X', 'p2': 'O'}
        elif choice == 'O':
            players = {'p1': 'O', 'p2': 'X'}
        else:
            print('')
            print('Incorrect selection')
    return players

# board display
def board_display(values):
    print(f' {values[0]} | {values[1]} | {values[2]}')
    print('-----------')
    print(f' {values[3]} | {values[4]} | {values[5]}')
    print('-----------')
    print(f' {values[6]} | {values[7]} | {values[8]}')

# checks for win
def win_check(board):
    win = False
    winning_moves = [
        [0, 1, 2],
        [0, 4, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 4, 6],
        [2, 5, 8],
        [3, 4, 5],
        [6, 7, 8]
    ]
    for moves in winning_moves:
        if board[moves[0]] == 'X' and board[moves[1]] == 'X' and board[moves[2]] == 'X' or board[moves[0]] == 'O' and board[moves[1]] == 'O' and board[moves[2]] == 'O':
            win = True
    return win

# makes a move
def make_move(player, board):
    move_made = None
    while move_made == None :
        print('')
        move = input(f'Player {player}, please select 1-9 to make a move: ')
        try:
            move = int(move)
        except:
            pass
        if move not in range(1, 10):
            print('')
            print('Incorrect choice, please try again.')
        elif board[move - 1] != ' ':
            print('')
            print('Position already taken!')
        else:
            move_made = move
    board[move_made - 1] = player
    return board

# switches player
def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

# asks if you want to play again, if you say N it exits the program
def play_again():
    again = None
    again = input('Would you like to play again? Y/N: ').upper()
    while again not in ['Y', 'N']:
        print('Incorrect choice.')
        again = input('Would you like to play again? Y/N: ').upper()
    if again == 'N':
        return False
    elif again == 'Y':
        return True

# main game function
def tic_tac_toe():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    won = False
    move_counter = 9
    welcome()
    players = player_select()
    current_player = players['p1']
    while won == False:
        os.system('clear')
        board_display(board)
        board = make_move(current_player, board)
        move_counter -= 1
        won = win_check(board)
        if won == True or move_counter == 0:
            os.system('clear')
            board_display(board)
            if won == True:
                print('')
                print(f'Player {current_player} is the winner!')
            elif move_counter == 0:
                print('')
                print("It's a tie!")
            again = play_again()
            if again:
                os.system('clear')
                board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                won = False
                move_counter = 9
                welcome()
                players = player_select()
                current_player = players['p1']
            else:
                os.system('clear')
                print('Thank you for playing, come again!')
                return
        else:
            current_player = switch_player(current_player)

# run the game!
tic_tac_toe()