from src.game import Game
from src.board import GameBoard
from src.player import Player

def main():
    Game(GameBoard(), (Player(symbol="X"), Player(symbol="O"))).start()

if __name__ == "__main__":
    main()