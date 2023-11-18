import pytest

from unittest import mock

from src.game import Game
from src.board import GameBoard
from src.player import Player

@mock.patch("src.game.get_input")
@mock.patch("src.player.get_input")
def test_valites_x_win_correctly(mock_player_input, mock_game_input, game: Game):
    mock_player_input.side_effect = ["1", "2", "4", "3", "7"]
    mock_game_input.return_value = "n"
    
    game.start()

    assert game.game_history[0] == {
        "winner": "X",
        "board": [
            ["X", "O", "O"],
            ["X", " ", " "],
            ["X", " ", " "],
        ]
    }

@mock.patch("src.game.get_input")
@mock.patch("src.player.get_input")
def test_valites_o_win_correctly(mock_player_input, mock_game_input, game: Game):
    mock_player_input.side_effect = ["1", "2", "3", "5", "4", "8"]
    mock_game_input.return_value = "n"
    
    game.start()

    assert game.game_history[0] == {
        "winner": "O",
        "board": [
            ["X", "O", "X"],
            ["X", "O", " "],
            [" ", "O", " "],
        ]
    }

@mock.patch("src.game.get_input")
@mock.patch("src.player.get_input")
def test_valites_tie_correctly(mock_player_input, mock_game_input, game: Game):
    mock_player_input.side_effect = ["1", "2", "3", "5", "4", "6", "8", "7", "9"]
    mock_game_input.return_value = "n"
    
    game.start()

    assert game.game_history[0] == {
        "winner": "Tie",
        "board": [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ]
    }


@pytest.fixture
def game() -> Game:
    return Game(GameBoard(), [Player(symbol="X"), Player(symbol="O")])
