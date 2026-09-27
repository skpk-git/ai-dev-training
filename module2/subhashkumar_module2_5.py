# subhashkumar_module2_5.py

# make X / O game to play using the terminal. 
# With two player each provide a number for corresponding choice. 

def display_board(board):
    """Display the X/O game board."""

    # Display the board using the numbers 1 to 9 as positions.
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board):
    """Check whether a player has won the game."""

    # Define all possible winning combinations.
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    # Check each possible winning combination.
    for first, second, third in winning_combinations:

        # Check whether the three positions contain the same symbol.
        if (board[first] == board[second] == board[third]
                and board[first] in ["X", "O"]):
            return board[first]

    # Return None if nobody has won yet.
    return None


def check_draw(board):
    """Check whether all positions have been used."""

    # Return True when there are no empty positions.
    return " " not in board


def play_game():
    """Run the two-player X/O game."""

    # Create an empty board with 9 positions.
    board = [" "] * 9

    # Start with Player 1 using X.
    current_player = "X"

    # Continue the game until there is a winner or draw.
    while True:

        # Display the current board.
        display_board(board)

        # Ask the current player to select a position.
        choice = input(
            f"Player {current_player}, choose a position (1-9): "
        )

        # Check that the input is a number.
        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        # Convert the input from text to an integer.
        position = int(choice)

        # Check that the number is between 1 and 9.
        if position < 1 or position > 9:
            print("Please choose a number from 1 to 9.")
            continue

        # Convert the position to a list index.
        index = position - 1

        # Check whether the position is already occupied.
        if board[index] != " ":
            print("That position is already taken. Choose another one.")
            continue

        # Put the player's X or O on the board.
        board[index] = current_player

        # Check whether the current player has won.
        winner = check_winner(board)

        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break

        # Check whether the game is a draw.
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            break

        # Change to the other player.
        current_player = "O" if current_player == "X" else "X"
            


# Start the game.
if __name__ == "__main__":
    play_game()