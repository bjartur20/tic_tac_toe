class GameBoard:
    def __init__(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def __str__(self):
        ret = f"{'-' * len(self.cells*2)}-\n"

        for row in self.cells:
            ret += f"|{'|'.join(row)}|\n"
            ret += f"{'-' * len(self.cells*2)}-\n"

        return ret

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
            self.__game_loop()
            play_again = self.__play_again()

    def __game_loop(self):
        current_turn = self.player_x
        while True:
            print(self.game_board)
            if current_turn == self.player_x:
                self.player_x.take_turn(self.game_board)
                current_turn = self.player_o
            else:
                self.player_o.take_turn(self.game_board)
                current_turn = self.player_x

    @staticmethod
    def __play_again(self):
        response = input("Would you like to play again? (y): ")
        return True if response == "y" else False

def main():
    Game().start()

if __name__ == "__main__":
    main()