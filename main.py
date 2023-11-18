from game import Game
from board import GameBoard
from player import Player

def main():
    Game(GameBoard(), [Player(symbol="X"), Player(symbol="O")]).start()

if __name__ == "__main__":
    main()