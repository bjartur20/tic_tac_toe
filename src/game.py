from src.board import GameBoard
from src.player import Player
from src.utils import get_input, get_game_board_string

class Game:
    def __init__(self, game_board: GameBoard, players: tuple[Player, Player]):
        self.game_board = game_board
        self.player_1 = players[0]
        self.player_2 = players[1]
        self.game_history = []

    def start(self):
        play_again = True
        
        while play_again:
            self.game_board.setup_game_board()
            self.__game_loop()
            play_again = self.__play_again()

        self.__display_end_message()

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
        
        self.__save_current_game()

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
        return get_input("Play again? (y/n): ") == "y"

    def __save_current_game(self):
        self.game_history.append({
            "winner": "Tie" if self.game_board.is_full else self.game_board.contains_winner(),
            "board": self.game_board.cells
        })

    def __display_end_message(self):
        print()
        print("Thank you for playing Tic-Tac-Toe")
        print("Here is a history of your games played during this session:")
        print()

        for index, game in enumerate(self.game_history):
            print(f"Game number {index + 1}")
            print(f"Winner: {game['winner']}")
            print(f"Endgame board:\n{get_game_board_string(game['board'])}")

