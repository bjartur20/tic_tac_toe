from src.board import GameBoard
from src.utils import get_input

class Player:
    def __init__(self, symbol: str):
        self.__symbol = symbol

    def take_turn(self, game_board: GameBoard):
        invalid_input = True
        print(f"{self.__symbol} player's turn")
        while invalid_input:
            response = get_input("Select a square (1-9): ")

            if not self.__validate_input(response, game_board):
                continue

            invalid_input = False
        
        game_board.place_symbol(self.__symbol, int(response)-1)

    def __validate_input(self, input_value: str, game_board: GameBoard) -> bool:
        if not input_value.isdigit():
            print(f"Please input a number")
            return False
        if not (1 <= int(input_value) <= 9):
            print(f"Please input a number between 1 and 9")
            return False
        if not game_board.is_cell_empty(int(input_value) - 1):
            print(f"Cell at position {input_value} has already been played")
            return False

        return True
