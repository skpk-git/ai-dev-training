# subhashkumar_module2_6.py

# make 2048 game to play using the terminal

import random
import os
import msvcrt

SIZE = 4


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
    print("Use the ARROW KEYS to move")
    print("Press Q to quit")


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
    # Check empty cells
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True

    # Check horizontal matches
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1]:
                return True

    # Check vertical matches
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

    # Arrow keys return two characters
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

    elif key in (b'q', b'Q'):
        return "QUIT"

    return None


def main():
    board = create_board()
    score = 0

    while True:
        print_board(board, score)

        if has_won(board):
            print("\nCongratulations! You reached 2048!")
            print("You can continue playing.")

        if not can_move(board):
            print("\nGAME OVER!")
            print(f"Final score: {score}")
            break

        key = get_key()

        if key == "QUIT":
            print("\nThanks for playing!")
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


if __name__ == "__main__":
    main()
