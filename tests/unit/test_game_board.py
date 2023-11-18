import pytest

from src.board import GameBoard

def test_is_full_returns_false_when_the_board_is_not_full(game_board: GameBoard):
    game_board.cells = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    assert game_board.is_full is False


def test_is_full_returns_true_when_the_board_is_full(game_board: GameBoard):
    game_board.cells = [
        ["X", "O", "O"],
        ["X", "O", "X"],
        ["O", "X", "X"],
    ]

    assert game_board.is_full is True


@pytest.mark.parametrize("cell_index,expected_coords", [
    [0, (0,0)], [1, (0, 1)], [2, (0, 2)], [3, (1, 0)], [4, (1, 1)], [5, (1, 2)], [6, (2, 0)], [7, (2, 1)], [8, (2, 2)]
])
def test_place_symbol_places_a_symbol_correctly_on_the_board(game_board: GameBoard, cell_index: int, expected_coords: tuple[int, int]):
    expected_cells = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    expected_cells[expected_coords[0]][expected_coords[1]] = "X"
    
    game_board.place_symbol("X", cell_index)

    assert game_board.cells == expected_cells


def test_contains_winner_returns_the_winner_when_a_winner_is_found_vertically(game_board: GameBoard):
    game_board.cells = [
        [" ", "X", " "],
        [" ", "X", " "],
        [" ", "X", " "],
    ]

    assert game_board.contains_winner() == "X"


def test_contains_winner_returns_the_winner_when_a_winner_is_found_horizontally(game_board: GameBoard):
    game_board.cells = [
        [" ", " ", " "],
        ["X", "X", "X"],
        [" ", " ", " "],
    ]

    assert game_board.contains_winner() == "X"


def test_contains_winner_returns_the_winner_when_a_winner_is_found_diagonally(game_board: GameBoard):
    game_board.cells = [
        ["X", " ", " "],
        [" ", "X", " "],
        [" ", " ", "X"],
    ]

    assert game_board.contains_winner() == "X"


def test_contains_winner_returns_none_when_no_winner_is_in_the_board(game_board: GameBoard):
    assert game_board.contains_winner() is None


@pytest.fixture
def game_board() -> GameBoard:
    game_board = GameBoard()
    game_board.setup_game_board()

    return game_board
