import pytest

from unittest import mock

from src.game import Game
from src.board import GameBoard
from src.player import Player

@mock.patch("src.game.get_input")
@mock.patch("src.player.get_input")
def test_valites_x_win_correctly(mock_player_input, mock_game_input, game: Game, player_x_winning_sequence: list[str]):
    mock_player_input.side_effect = player_x_winning_sequence
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
def test_valites_o_win_correctly(mock_player_input, mock_game_input, game: Game, player_o_winning_sequence: list[str]):
    mock_player_input.side_effect = player_o_winning_sequence
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
def test_valites_tie_correctly(mock_player_input, mock_game_input, game: Game, tie_sequence: list[str]):
    mock_player_input.side_effect = tie_sequence
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

@mock.patch("src.game.get_input")
@mock.patch("src.player.get_input")
def test_can_play_multiple_games_in_a_session(
    mock_player_input,
    mock_game_input,
    game: Game,
    player_x_winning_sequence: list[str],
    player_o_winning_sequence: list[str],
    tie_sequence: list[str]
):
    mock_player_input.side_effect = player_x_winning_sequence + player_o_winning_sequence + tie_sequence
    mock_game_input.side_effect = ["y", "y", "n"]
    
    game.start()

    assert game.game_history == [
        {
            "winner": "X",
            "board": [
                ["X", "O", "O"],
                ["X", " ", " "],
                ["X", " ", " "],
            ]
        },
        {
            "winner": "O",
            "board": [
                ["X", "O", "X"],
                ["X", "O", " "],
                [" ", "O", " "],
            ]
        },
        {
            "winner": "Tie",
            "board": [
                ["X", "O", "X"],
                ["X", "O", "O"],
                ["O", "X", "X"],
            ]
        }
    ]


@pytest.fixture
def game() -> Game:
    return Game(GameBoard(), [Player(symbol="X"), Player(symbol="O")])


@pytest.fixture
def player_x_winning_sequence() -> list[str]:
    return ["1", "2", "4", "3", "7"]

@pytest.fixture
def player_o_winning_sequence() -> list[str]:
    return ["1", "2", "3", "5", "4", "8"]

@pytest.fixture
def tie_sequence() -> list[str]:
    return ["1", "2", "3", "5", "4", "6", "8", "7", "9"]

