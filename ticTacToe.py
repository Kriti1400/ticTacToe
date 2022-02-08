# This program is a Tic Tac Toe game that can be played via the command line
# Created with reference from Geoffrey Mariette's betterprogramming article

# display_board() replaces each number in the board list with either X or O
#  or a blank space
def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""
    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
            # this replaces the ith location on the board with 'O' or 'X'  
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
            # this replaces the ith location on the board with a blank space
    print(blankBoard)

# player_choice() allows player 1 to select their symbol and assigns the other
#  symbol to player 2
def player_choice():
    player1 = input("Player 1: Enter either 'X' or 'O' to select your symbol ")
    while True:
        if player1 == "X":
            player2 = "O"
            print("Player 1 is " + player1 + " and Player 2 is " + player2 + ".")
            return player1, player2
        elif player1 == "O":
            player2 = "X"
            print("Player 1 is " + player1 + " and Player 2 is " + player2 + ".")
            return player1, player2
        else:
            player1 = input("Invalid Input! Player 1: Please enter either 'X' or 'O' to select your symbol ")
            

# place_marker(board, location, symbol) replaces the location of board with symbol
def place_marker(board, location, symbol):
    board[location] = symbol
    return board

# choose_place(board) prompts the player to select the next location for their symbol until
#   they select an empty location
def choose_place(board):
    place = input("Choose an empty space between 1 and 9 to make your move: ")
    while True:
        if place.isdigit() == False:
            place = input("Invalid Input! Choose an empty space between 1 and 9 to make your move: ")
        if int(place) > 9 or int(place) < 1:
            place = input("Invalid Input! Choose an empty space between 1 and 9 to make your move: ")
        if place_check(board, int(place)):
            return place
        else:
            place = input("Invalid Input! Choose an empty space between 1 and 9 to make your move: ")

# place_check(board, location) returns true if the board location is free and false otherwise
def place_check(board, location):
    return board[location] == '#'

# winner_check(board, symbol) checks the board to see if the player with symbol won
def winner_check(board, symbol):
    if board[1] == board[2] == board[3] == symbol:
        return True
    if board[4] == board[5] == board[6] == symbol:
        return True
    if board[7] == board[8] == board[9] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    if board[3] == board[6] == board[9] == symbol:
        return True
    if board[1] == board[5] == board[9] == symbol:
        return True
    if board[3] == board[5] == board[7] == symbol:
        return True
    return False

# full_board_check(board) returns true if the board is full and false otherwise
def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    # Counter keeps track of who is currently playing
    i = 1
    # Initial symbol selection
    players=player_choice()
    # Creates an empty board
    board = ['#'] * 10
    while True:
        # Game setup
        game_on=full_board_check(board)
        while not game_on:
            # Player decides where to put the symbol
            position = choose_place(board)
            # Checks which symbol to place on board
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            place_marker(board, int(position), marker)
            # Check the board
            display_board(board)
            i += 1
            if i == 10:
                print("There is a tie!")
                quit()
            if winner_check(board, marker):
                if i % 2 == 0:
                    print("Player 1 won!")
                    quit()
                else:
                    print("Player 2 won!")
                    quit()
