from src.board import GameBoard
from src.utils import get_input

class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def take_turn(self, game_board: GameBoard):
        invalid_input = True
        print(f"{self.symbol} player's turn")
        while invalid_input:
            response = get_input("Select a square (1-9): ")

            if not response.isdigit():
                print(f"Please input a number")
                continue
            if not (1 <= int(response) <= 9):
                print(f"Please input a number between 1 and 9")
                continue
            if not game_board.is_cell_empty(int(response) - 1):
                print(f"Cell at position {response} has already been played")
                continue

            invalid_input = False
        
        game_board.place_symbol(self.symbol, int(response)-1)
