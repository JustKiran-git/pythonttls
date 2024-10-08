def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_board_full(board):
    """Checks if the board is full."""
    return all(space in ['X', 'O'] for space in board)
def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [' '] * 9  # Initialize the board
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("The chosen position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
if __name__ == "__main__":
    tic_tac_toe()
