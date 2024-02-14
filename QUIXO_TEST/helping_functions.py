from game import Move
import numpy as np

def get_all_legal_moves(player, board, board_size=5):

    moves = []

    # Generate moves for corners, edges , etc of the board
    for x in [0, board_size - 1]:
        for y in [0, board_size - 1]:

            # Check if the move is legal
            if board[y][x] == player or board[y][x] == -1:

                if x == 0 and y == 0:
                    moves.append(((x, y), Move.RIGHT))
                    moves.append(((x, y), Move.BOTTOM))
                elif x == 0 and y == board_size - 1:
                    moves.append(((x, y), Move.RIGHT))
                    moves.append(((x, y), Move.TOP))
                elif x == board_size - 1 and y == 0:
                    moves.append(((x, y), Move.BOTTOM))
                    moves.append(((x, y), Move.LEFT))
                elif x == board_size - 1 and y == board_size - 1:
                    moves.append(((x, y), Move.TOP))
                    moves.append(((x, y), Move.LEFT))

    for x in [0, board_size - 1]:
        for y in range(1, board_size - 1):

            # Check if the move is legal
            if board[y][x] == player or board[y][x] == -1:

                moves.append(((x, y), Move.TOP))
                moves.append(((x, y), Move.BOTTOM))
                if x == 0:
                    moves.append(((x, y), Move.RIGHT))
                else:
                    moves.append(((x, y), Move.LEFT))

    for x in range(1, board_size - 1):
        for y in [0, board_size - 1]:

            # Check if the move is legal (either an empty spot or the player's piece)
            if board[y][x] == player or board[y][x] == -1:

                moves.append(((x, y), Move.RIGHT))
                moves.append(((x, y), Move.LEFT))
                if y == 0:
                    moves.append(((x, y), Move.BOTTOM))
                else:
                    moves.append(((x, y), Move.TOP))
    return moves

def get_possible_moves(board, player):

    legal_moves = []

    # Get all legal possible moves in the game
    legal_moves = get_all_legal_moves(player, board, len(board))

    #Shuffle legal_moves to not analyse moves in order
    np.random.shuffle(legal_moves)
    
    return legal_moves

def find_max_sequence(player, board, board_size=5):

    max_sequence_length = 0

    # Check rows for pieces
    for i in range(board_size):
        row_count = sum(1 for j in range(board_size) if board[i][j] == player)
        max_sequence_length = max(max_sequence_length, row_count)

    # Check columns for pieces
    for j in range(board_size):
        col_count = sum(1 for i in range(board_size) if board[i][j] == player)
        max_sequence_length = max(max_sequence_length, col_count)

    # Check main diagonal \
    diag_count1 = sum(1 for i in range(board_size) if board[i][i] == player)

    # Check secondary diagonal /
    diag_count2 = sum(1 for i in range(board_size) if board[i][board_size - 1 - i] == player)

    max_sequence_length = max(max_sequence_length, diag_count1, diag_count2)

    return max_sequence_length

def get_intermediate_state_evaluation(player, board):

    max_sequence_length_player = 0
    max_sequence_length_opponent = 0

    opponent = (player + 1)%2

    max_sequence_length_player = find_max_sequence(player, board, len(board))
    max_sequence_length_opponent = find_max_sequence(opponent, board, len(board))

    return max_sequence_length_player - max_sequence_length_opponent
