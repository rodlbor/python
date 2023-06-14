import chess
import random

def print_board(board):
    print(board)

def get_user_move(board):
    while True:
        user_input = input("Enter your move (e.g., 'e2e4'): ")
        try:
            move = chess.Move.from_uci(user_input)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
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
