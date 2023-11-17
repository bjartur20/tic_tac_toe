class GameBoard:
    def setup_game_board(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def __str__(self) -> str:
        ret = f"{'-' * len(self.cells*2)}-\n"

        for row in self.cells:
            ret += f"|{'|'.join(row)}|\n"
            ret += f"{'-' * len(self.cells*2)}-\n"

        return ret

    @property
    def is_full(self) -> bool:
        return all([cell != " " for row in self.cells for cell in row])

    def place_symbol(self, symbol: str, place: int):
        row = place // 3
        col = place % 3
        self.cells[row][col] = symbol

class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.score = 0

    def take_turn(self, game_board: GameBoard):
        response = input("Select a square (1-9): ")
        game_board.place_symbol(self.symbol, int(response)-1)

class Game:
    def __init__(self):
        self.game_board = GameBoard()
        self.player_x = Player(symbol="X")
        self.player_o = Player(symbol="O")

    def start(self):
        play_again = True
        while play_again:
            self.game_board.setup_game_board()
            self.__game_loop()
            play_again = self.__play_again()

    def __game_loop(self):
        game_running = True
        current_turn = self.player_x
        while game_running:
            print(self.game_board)
            if current_turn == self.player_x:
                self.player_x.take_turn(self.game_board)
                current_turn = self.player_o
            else:
                self.player_o.take_turn(self.game_board)
                current_turn = self.player_x

            game_running = not self.__is_game_finished()

    def __is_game_finished(self) -> bool:
        if self.game_board.is_full:
            print("Tie!")
            return True

        return False


    @staticmethod
    def __play_again() -> bool:
        response = input("Would you like to play again? (y): ")
        return response == "y"

def main():
    Game().start()

if __name__ == "__main__":
    main()