tic_tac_toe_board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
player_turn = "X"
winner = False
game_tie = False


def display_board():  # Print out tic tac toe board
    print(tic_tac_toe_board[0] + "|" + tic_tac_toe_board[1] + "|" + tic_tac_toe_board[2])
    print(tic_tac_toe_board[3] + "|" + tic_tac_toe_board[4] + "|" + tic_tac_toe_board[5])
    print(tic_tac_toe_board[6] + "|" + tic_tac_toe_board[7] + "|" + tic_tac_toe_board[8])


def play_game():
    print("X will start!")
    display_board()
    while winner is False:  # Game will continue to run until there is a winner
        handle_turn()
        is_winner()
        is_tie()

        if game_tie:  # Game will also end if there is a tie
            break
        switch_turn()
        if winner is False:  # Displaying whose turn it is
            print("It is now " + player_turn + "'s turn.")


def handle_turn():  # Asking the user for input and displaying the corresponding player onto the board
    position = input("Choose number 1-9:")
    position = int(position) - 1
    if tic_tac_toe_board[position] == "-":
        if player_turn == "X":
            tic_tac_toe_board[position] = "X"
            display_board()
        else:
            tic_tac_toe_board[position] = "O"
            display_board()
    else:  # If a player picks a spot that is already occupied
        display_board()
        position = input("You can not go there! Please pick another number 1-9:")
        position = int(position) - 1
        tic_tac_toe_board[position] = player_turn
        display_board()


def is_winner():  # Determine if game is won
    global winner

    if ((tic_tac_toe_board[0] == tic_tac_toe_board[1] == tic_tac_toe_board[2] != "-") or  # Winner top row
            (tic_tac_toe_board[3] == tic_tac_toe_board[4] == tic_tac_toe_board[5] != "-") or  # Winner middle row
            (tic_tac_toe_board[6] == tic_tac_toe_board[7] == tic_tac_toe_board[8] != "-") or  # Winner bottom row
            (tic_tac_toe_board[0] == tic_tac_toe_board[3] == tic_tac_toe_board[6] != "-") or  # Winner left column
            (tic_tac_toe_board[1] == tic_tac_toe_board[4] == tic_tac_toe_board[7] != "-") or  # Winner middle column
            (tic_tac_toe_board[2] == tic_tac_toe_board[5] == tic_tac_toe_board[8] != "-") or  # Winner right column
            (tic_tac_toe_board[0] == tic_tac_toe_board[4] == tic_tac_toe_board[8] != "-") or  # Winner diagonal
            (tic_tac_toe_board[2] == tic_tac_toe_board[4] == tic_tac_toe_board[6] != "-")):  # Winner diagonal
        winner = True
        print("Congratulations, " + player_turn + " you win!")


def switch_turn():  # Changing the players turn
    global player_turn
    if player_turn == "X":
        player_turn = "O"
    elif player_turn == "O":
        player_turn = "X"


def is_tie():  # Determining if the game is a tie
    global game_tie
    if "-" not in tic_tac_toe_board and winner is False:
        print("The game is a tie!")
        game_tie = True


play_game()  # Start game
