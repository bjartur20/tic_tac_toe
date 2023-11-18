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

    def place_symbol(self, symbol: str, idx: int):
        self.cells[idx // 3][idx % 3] = symbol

    def contains_winner(self) -> str | None:
        # TODO: Might be able to refactor this function

        for i in range(len(self.cells) - 1):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] != " ":
                return self.cells[i][0]
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] != " ":
                return self.cells[i][0]
        
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != " ":
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != " ":
            return self.cells[0][2]

class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

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
        print(self.game_board)
        while game_running:
            if current_turn == self.player_x:
                self.player_x.take_turn(self.game_board)
                current_turn = self.player_o
            else:
                self.player_o.take_turn(self.game_board)
                current_turn = self.player_x

            print(self.game_board)
            game_running = not self.__is_game_finished()

    def __is_game_finished(self) -> bool:
        if winner := self.game_board.contains_winner():
            print(f"Player {winner} wins!")
            return True
        if self.game_board.is_full:
            print("Tie!")
            return True

        return False


    @staticmethod
    def __play_again() -> bool:
        return input("Would you like to play again? (y/n): ") == "y"

def main():
    Game().start()

if __name__ == "__main__":
    main()