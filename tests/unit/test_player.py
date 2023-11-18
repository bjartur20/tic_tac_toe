import pytest

from unittest import mock

from src.player import Player

@pytest.mark.parametrize(
        "input_square,expected_square",
        [
            ["1", 0],
            ["9", 8]
        ]
)
@mock.patch("src.player.get_input")
def test_take_turn_places_the_players_symbol_on_the_board_when_called_with_numbers_between_1_and_9(
    mock_get_input, player: Player, input_square: str, expected_square: int
):
    mock_get_input.return_value = input_square
    mock_game_board = mock.MagicMock()

    player.take_turn(mock_game_board)

    mock_game_board.place_symbol.assert_called_once_with("X", expected_square)


@pytest.mark.parametrize(
        "input_square",
        [
            "0",
            "10",
            "99999",
            "one"
        ]
)
@mock.patch("src.player.get_input")
def test_take_turn_asks_for_new_input_when_called_with_input_outside_1_and_9_or_character(
    mock_input, player: Player, input_square: str
):
    mock_input.side_effect = [input_square, "1"]

    player.take_turn(mock.MagicMock())

    assert mock_input.call_count == 2


@mock.patch("src.player.get_input")
def test_take_turn_asks_for_new_input_when_called_with_square_that_is_already_occupied(
    mock_input, player: Player
):
    mock_game_board = mock.MagicMock()
    mock_game_board.is_cell_empty.side_effect = [False, True]
    mock_input.side_effect = ["1", "2"]

    player.take_turn(mock_game_board)

    assert mock_input.call_count == 2


@pytest.fixture
def player():
    return Player(symbol="X")
