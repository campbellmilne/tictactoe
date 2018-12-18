import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('\n')

def marker_assign():
    markers = ""
    marker = input("Player 1, would you like to be X or O?: ").upper()
    if marker == "X":
        return ("X", "O")
    elif marker == "O":
        return ("O", "X")
    else:
        print("Sorry, that's not a valid selection")
    return markers

def first_turn():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"
    return turn

def move(board,marker):
    position = int(input("Select a square (1-9): "))
    if position > 9 or position < 1:
        print("Sorry, that move is invalid")
    elif board[position] == " ":
        board[position] = marker
        return board
    else:
        print("Sorry, that move has already been played.")

def win_check(board,marker):
    return((board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[7] == marker and board[4] == marker and board[1] == marker) or
    (board[8] == marker and board[5] == marker and board[2] == marker) or
    (board[9] == marker and board[6] == marker and board[3] == marker) or
    (board[7] == marker and board[5] == marker and board[3] == marker) or
    (board[1] == marker and board[5] == marker and board[9] == marker))

def full_check(board):
    return " " not in board

def replay():
    return input("Play again? ").lower().startswith("y")

print("Welcome to Tic-Tac-Toe")
playing = True
while playing:

    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1,player2 = marker_assign()
    turn = first_turn()
    while True:
        if turn == "Player 1":
            print("Player 1's turn: ")
            display_board(board)
            move(board,player1)
            if win_check(board,player1):
                display_board(board)
                print("Player 1 has won the game.")
                break
            elif full_check(board):
                print("It's a tie.")
                break
            else:
                turn = "Player 2"

        if turn == "Player 2":
            print("Player 2's turn: ")
            display_board(board)
            move(board,player2)
            if win_check(board,player2):
                display_board(board)
                print("Player 2 has won the game.")
                break
            elif full_check(board):
                print("It's a tie.")
                break
            else:
                turn = "Player 1"

    if not replay():
        break


print("Goodbye.")
