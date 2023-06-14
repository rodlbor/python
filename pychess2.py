import chess
import random

# ASCII art representation of the pieces
PIECE_ART = {
    chess.PAWN: " ♟ ",
    chess.KNIGHT: " ♞ ",
    chess.BISHOP: " ♝ ",
    chess.ROOK: " ♜ ",
    chess.QUEEN: " ♛ ",
    chess.KING: " ♚ ",
}

def print_board(board):
    print("\n   a  b  c  d  e  f  g  h")
    print("  ------------------------")
    for rank in range(7, -1, -1):
        print(chess.RANK_NAMES[rank] + "|", end="")
        for file in chess.FILE_NAMES:
            square = chess.square(chess.FILE_NAMES.index(file), rank)
            piece = board.piece_at(square)
            if piece:
                print(PIECE_ART[piece.piece_type], end="")
            else:
                print(" . ", end="")
        print("|")
    print("  ------------------------")
    print("   a  b  c  d  e  f  g  h")

def get_user_move(board):
    while True:
        user_input = input("Enter your move (e.g., 'e2e4'): ")
        if len(user_input) == 4:
            try:
                from_square = chess.parse_square(user_input[:2])
                to_square = chess.parse_square(user_input[2:])
                move = chess.Move(from_square, to_square)
                if move in board.legal_moves:
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")

def get_ai_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def play_game():
    board = chess.Board()
    
    while not board.is_game_over():
        print_board(board)
        
        # Player's move
        user_move = get_user_move(board)
        board.push(user_move)
        
        if board.is_game_over():
            break
        
        # AI's move
        ai_move = get_ai_move(board)
        board.push(ai_move)
        
    print_board(board)
    result = board.result()
    print("Game over. Result: " + result)

# Start the game
play_game()
