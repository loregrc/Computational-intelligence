from game import Player, Move
from game2 import Game2 as Game
import random
from helping_functions import get_possible_moves, get_intermediate_state_evaluation
from copy import deepcopy

class MiniMaxPlayer(Player):
    def __init__(self, max_depth):

        super().__init__()
        self.player = None
        self.max_depth = max_depth

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:

        best_points = float("-inf")
        best_move = None
        current_player = game.get_current_player()
        self.player = current_player

        moves = get_possible_moves(game.get_board(), current_player)

        alpha = float("-inf")
        beta = float("inf")

        for move in moves:

            board = deepcopy(game.get_board())
            game_cloned = Game(board, game.get_current_player())
            game_cloned.move(move[0], move[1], current_player)

            points = self.minimax(game_cloned, self.max_depth, alpha, beta, False)
            if points > best_points:
                best_points = points
                best_move = move
            alpha = max(alpha, best_points)
            if beta <= alpha:
                break

        # Return the best move, or a random move if no best move is found
        if best_move:
            return best_move
        else: 
            return random.choice(moves)

    def minimax(self, game, depth, alpha, beta, findingMax):
        # Minimax algorithm with alpha-beta pruning
        current_player = game.get_current_player()

        if depth == 0 or game.check_winner() != -1:
            # Evaluate the game if it's at max depth or there is a winner
            return self.evaluate_state(game)

        if findingMax:
            max_evaluation = float("-inf")

            #print(f'player MAXIMIZING:{current_player}')

            for move in get_possible_moves(game.get_board(), current_player):

                game_cloned = game.clone()
                game_cloned.move(move[0], move[1], current_player)

                eval = self.minimax(game_cloned, depth - 1, alpha, beta, False)
                max_evaluation = max(max_evaluation, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_evaluation
        else:
            min_evaluation = float("inf")

            #Switching player to minimize opponent's state 
            current_player = (self.player + 1)%2

            #print(f'player minimizing:{current_player}')

            for move in get_possible_moves(game.get_board(), current_player):

                game_cloned = game.clone()
                game_cloned.move(move[0], move[1], current_player)

                eval = self.minimax(game_cloned, depth - 1, alpha, beta, True)
                min_evaluation = min(min_evaluation, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_evaluation

    def evaluate_state(self, game):

        winner = game.check_winner()

        if winner == self.player:
            return 5
        elif winner != -1:
            return -5

        return get_intermediate_state_evaluation(self.player, game.get_board())