from game import Move, Game, Player
from copy import deepcopy
from helping_functions import get_all_legal_moves

# ANSI escape codes for colors
GREEN = '\033[92m'  # Green color
RED = '\033[91m'  # Red color
RESET = '\033[0m'  # Reset color to default

X_SYMBOL = 'X'  # X symbol
O_SYMBOL = 'O'  # O symbol

class Game2(Game):
    def __init__(self, board, current_player) -> None:
        super().__init__()
        self._board = board
        self.current_player_idx = current_player
    
    def move(self, from_pos: tuple[int, int], slide: Move, player_id: int) -> bool:
        return super()._Game__move(from_pos, slide, player_id)
    
    def clone(self):
        board = deepcopy(self._board)
        return Game2(board, self.current_player_idx)
    
    def print_board(self):
        '''Prints the board with coordinates. -1 are neutral pieces, 0 are pieces of player 0, 1 pieces of player 1'''

        # Print column numbers
        print(" ", end=" ")
        for x in range(len(self._board)):
            print(x, end=" ")
        print()  # New line

        row_count = 0

        for row in self._board:
            
            # Print row number
            print(row_count, end=" ")
            row_count += 1

            for cell in row:
                if cell == -1:
                    print("-", end=" ")
                elif cell == 0:
                    # Print the X symbol in red
                    print(RED+X_SYMBOL+RESET, end=" ")
                elif cell == 1:
                    # Print the O symbol in green
                    print(GREEN+O_SYMBOL+RESET, end=" ")
            print()  # Print a new line after each row

    def play(self, player1: Player, player2: Player) -> int:
        '''Play the game. Returns the winning player'''

        self.print_board()
        print()
        
        players = [player1, player2]
        winner = -1
        while winner < 0:
            self.current_player_idx += 1
            self.current_player_idx %= len(players)
            ok = False
            while not ok:
                from_pos, slide = players[self.current_player_idx].make_move(
                    self)
                
                ok = self.move(from_pos, slide, self.current_player_idx)

                if ok:
                    print(from_pos, slide)
                    self.print_board()
                    print()

            winner = self.check_winner()
        return winner
    
    def is_valid_move(self, row, column, direction, player):

        move = (row, column), direction

        legal_moves = get_all_legal_moves(player, self._board, len(self._board))

        if move in legal_moves:
            return True
        else:
            return False