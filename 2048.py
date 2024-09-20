import random

def initialize_game():
    """Create a 4x4 grid and add two random tiles."""
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    """Add a random tile (2 or 4) to an empty space on the board."""
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 4 if random.random() < 0.1 else 2

def print_board(board):
    """Display the game board."""
    for row in board:
        print("\t".join(str(num) if num > 0 else '.' for num in row))
    print()

def slide_and_merge(row):
    """Slide and merge a single row to the left."""
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False

    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i < len(new_row) - 1 and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])

    merged_row += [0] * (4 - len(merged_row))  # Fill with zeros
    return merged_row

def move(board, direction):
    """Move the tiles in the specified direction."""
    if direction == 'left':
        for i in range(4):
            board[i] = slide_and_merge(board[i])
    elif direction == 'right':
        for i in range(4):
            board[i] = slide_and_merge(board[i][::-1])[::-1]
    elif direction == 'up':
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            new_column = slide_and_merge(column)
            for i in range(4):
                board[i][j] = new_column[i]
    elif direction == 'down':
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            new_column = slide_and_merge(column[::-1])[::-1]
            for i in range(4):
                board[i][j] = new_column[i]

def check_game_over(board):
    """Check if the game is over."""
    if any(2048 in row for row in board):
        print("You win!")
        return True
    if all(board[r][c] != 0 for r in range(4) for c in range(4)):
        for r in range(4):
            for c in range(4):
                if (r < 3 and board[r][c] == board[r + 1][c]) or (c < 3 and board[r][c] == board[r][c + 1]):
                    return False
        print("Game Over!")
        return True
    return False

def main():
    """Run the main game loop."""
    board = initialize_game()
    print_board(board)

    while True:
        move_input = input("Enter move (w/a/s/d): ").strip().lower()
        if move_input in ['w', 'a', 's', 'd']:
            move(board, {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}[move_input])
            add_random_tile(board)
            print_board(board)
            if check_game_over(board):
                break
        else:
            print("Invalid input! Use w, a, s, d.")

if __name__ == "__main__":
    main()
