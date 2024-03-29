from game import Player, Move
from game2 import Game2 as Game
import keyboard


class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.player = None

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:

        current_player = game.get_current_player()
        self.player = current_player


        while True:
            try:
                move_input = input("Enter your move (format: 'COLUMN ROW direction'): ")

                if keyboard.is_pressed('esc'):
                    raise KeyboardInterrupt

                move_parts = move_input.split()
                if len(move_parts) != 3:
                    raise ValueError("Invalid input format. Please enter COLUMN, ROW, and direction separated by spaces.")
                
                column = int(move_parts[0])
                row = int(move_parts[1])
                direction = Move[move_parts[2].upper()]
                
                if not game.is_valid_move(column, row, direction, current_player):
                    print("Invalid move. Please try again.")
                    continue
                
                return (column, row), direction
            except ValueError as ve:
                print(ve)
            except KeyError:
                print("Invalid direction.")