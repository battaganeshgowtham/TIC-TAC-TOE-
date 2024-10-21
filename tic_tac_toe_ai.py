def is_winner(board, player):
    # Check if the player has won the game
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def is_draw(board):
    # Check if the game is a draw
    return " " not in board

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, "O"):
        return -1
    if is_winner(board, "X"):
        return 1
    if is_draw(board):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def play_tic_tac_toe():
    board = [" "] * 9
    player = "X"

    print("Tic-Tac-Toe Game")

    while True:
        print_board(board)

        if player == "X":
            move = int(input("Enter your move (0-8): "))
            if board[move] == " ":
                board[move] = player
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            move = find_best_move(board)
            board[move] = player

        if is_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "X" if player == "O" else "O"

if __name__ == "__main__":
    play_tic_tac_toe()
