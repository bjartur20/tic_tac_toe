from board import GameBoard
from player import Player

class Game:
    def __init__(self, game_board: GameBoard, players: list[Player]):
        self.game_board = game_board
        self.player_1 = players[0]
        self.player_2 = players[1]

    def start(self):
        play_again = True
        while play_again:
            self.game_board.setup_game_board()
            self.__game_loop()
            play_again = self.__play_again()

    def __game_loop(self):
        game_running = True
        current_turn = self.player_1
        print(self.game_board)
        while game_running:
            if current_turn == self.player_1:
                self.player_1.take_turn(self.game_board)
                current_turn = self.player_2
            else:
                self.player_2.take_turn(self.game_board)
                current_turn = self.player_1

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
