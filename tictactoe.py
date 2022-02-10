# welcome DONE
# player selection DONE
# board display
# player move
# check combination
# if game won end game, if not, continue until board is full
# display results

# welcome message
def welcome():
    print('Welcome to Tic Tac Toe!')

# player selection
def player_select():
    players = {'p1': None, 'p2': None}
    while players['p1'] == None:
        choice = input('Will Player One be "X" or "O"? ').upper()
        if choice == 'X':
            players = {'p1': 'X', 'p2': 'O'}
        elif choice == 'O':
            players = {'p1': 'O', 'p2': 'X'}
        else:
            print('Incorrect selection')
    return players

# board display
def board_display(values=[' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    print(f' {values[0]} | {values[1]} | {values[2]}')
    print('-----------')
    print(f' {values[3]} | {values[4]} | {values[5]}')
    print('-----------')
    print(f' {values[6]} | {values[7]} | {values[8]}')

def win_check(combo):
    winning_moves

def tic_tac_toe():
    welcome()
    players = player_select()

tic_tac_toe()