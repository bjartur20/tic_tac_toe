from src.board import GameBoard
from src.utils import get_input

class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def take_turn(self, game_board: GameBoard):
        invalid_input = True
        while invalid_input:
            response = get_input("Select a square (1-9): ")
            if response.isdigit() and (1 <= int(response) <= 9):
                invalid_input = False
            print(f"Player {self.symbol}, please input a number between 1 and 9")
        

        game_board.place_symbol(self.symbol, int(response)-1)
