# subhashkumar_module2_7.py

# adjust the code you made to store the current session in a file and user can continue later. 

import random
import os
import msvcrt
import json

SIZE = 4
SAVE_FILE = "2048_save.json"


def clear_screen():
    os.system("cls")


def create_board():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board):
    empty = []

    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                empty.append((r, c))

    if empty:
        r, c = random.choice(empty)
        board[r][c] = 4 if random.random() < 0.1 else 2


def save_game(board, score):
    game_data = {
        "board": board,
        "score": score
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(game_data, file)

    print("\nGame saved.")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r") as file:
            game_data = json.load(file)

        board = game_data["board"]
        score = game_data["score"]

        return board, score

    except (json.JSONDecodeError, KeyError):
        print("Save file is corrupted.")
        return None


def print_board(board, score):
    clear_screen()

    print("=" * 29)
    print("          2048 GAME")
    print("=" * 29)
    print(f"Score: {score}")
    print()

    for row in board:
        print("+------+------+------+------+")
        print("|", end="")

        for value in row:
            if value == 0:
                print("      |", end="")
            else:
                print(f"{value:^6}|", end="")

        print()

    print("+------+------+------+------+")
    print()
    print("Use ARROW KEYS to move")
    print("Press Q to quit and save")


def compress(row):
    return [value for value in row if value != 0]


def merge(row):
    result = []
    score = 0
    i = 0

    while i < len(row):

        if i + 1 < len(row) and row[i] == row[i + 1]:
            new_value = row[i] * 2

            result.append(new_value)

            score += new_value

            i += 2

        else:
            result.append(row[i])

            i += 1

    return result, score


def move_left(board):
    changed = False
    score = 0

    for r in range(SIZE):

        original = board[r][:]

        row = compress(board[r])

        row, gained = merge(row)

        row += [0] * (SIZE - len(row))

        board[r] = row

        score += gained

        if original != row:
            changed = True

    return changed, score


def move_right(board):

    for r in range(SIZE):
        board[r].reverse()

    changed, score = move_left(board)

    for r in range(SIZE):
        board[r].reverse()

    return changed, score


def move_up(board):

    board[:] = [list(row) for row in zip(*board)]

    changed, score = move_left(board)

    board[:] = [list(row) for row in zip(*board)]

    return changed, score


def move_down(board):

    board[:] = [list(row) for row in zip(*board)]

    changed, score = move_right(board)

    board[:] = [list(row) for row in zip(*board)]

    return changed, score


def can_move(board):

    # Empty cell available
    for r in range(SIZE):
        for c in range(SIZE):

            if board[r][c] == 0:
                return True

    # Horizontal matches
    for r in range(SIZE):

        for c in range(SIZE - 1):

            if board[r][c] == board[r][c + 1]:
                return True

    # Vertical matches
    for r in range(SIZE - 1):

        for c in range(SIZE):

            if board[r][c] == board[r + 1][c]:
                return True

    return False


def has_won(board):

    for row in board:

        if 2048 in row:
            return True

    return False


def get_key():

    key = msvcrt.getch()

    # Arrow keys
    if key == b'\xe0':

        key = msvcrt.getch()

        if key == b'H':
            return "UP"

        elif key == b'P':
            return "DOWN"

        elif key == b'K':
            return "LEFT"

        elif key == b'M':
            return "RIGHT"

    # Quit
    elif key in (b'q', b'Q'):

        return "QUIT"

    return None


def ask_continue():

    save = load_game()

    if save is None:

        return create_board(), 0

    print("A previous game was found.")

    print()
    print("Press Y to continue")
    print("Press N to start a new game")

    while True:

        key = msvcrt.getch().lower()

        if key == b'y':

            return save

        elif key == b'n':

            return create_board(), 0


def main():

    board, score = ask_continue()

    while True:

        print_board(board, score)

        if has_won(board):

            print("\nCongratulations! You reached 2048!")

            print("You can continue playing.")

        if not can_move(board):

            print("\nGAME OVER!")

            print(f"Final score: {score}")

            # Remove completed game save
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)

            break

        key = get_key()

        if key == "QUIT":

            save_game(board, score)

            print("\nGame saved.")

            print("You can continue later.")

            break

        if key == "UP":

            changed, gained = move_up(board)

        elif key == "DOWN":

            changed, gained = move_down(board)

        elif key == "LEFT":

            changed, gained = move_left(board)

        elif key == "RIGHT":

            changed, gained = move_right(board)

        else:

            continue

        if changed:

            score += gained

            add_random_tile(board)

            # Automatically save after every move
            save_game(board, score)


if __name__ == "__main__":
    main()