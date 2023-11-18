from unittest import mock

from src.game import Game

@mock.patch("src.game.get_input")
def test_start_sets_up_the_board(mock_get_input):
    # mock_get_input.side_effect = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "n"]
    mock_game_board = mock.MagicMock()
    mock_players = [
        mock.MagicMock(),
        mock.MagicMock()
    ]
    game = Game(mock_game_board, mock_players)

    game.start()

    mock_game_board.setup_game_board.assert_called()