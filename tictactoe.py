# tic_tac_toe.py

board = [' '] * 9
game_over = False
current_player = 'X'

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def make_move(position):
    global current_player
    if board[position] == ' ':
        board[position] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print('Position already taken!')

def check_win():
    global game_over
    if board[0] == board[1] == board[2] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[3] == board[4] == board[5] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[6] == board[7] == board[8] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[0] == board[3] == board[6] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[1] == board[4] == board[7] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[2] == board[5] == board[8] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[0] == board[4] == board[8] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif board[2] == board[4] == board[6] != ' ':
        print(current_player + ' wins!')
        game_over = True
    elif ' ' not in board:
        print('It\'s a tie!')
        game_over = True

print_board()
while not game_over:
    print('Current player: ' + current_player)
    position = int(input('Enter position (0-8): '))
    make_move(position)
    print_board()
    check_win()
