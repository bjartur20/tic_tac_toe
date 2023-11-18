def get_input(text: str) -> str:
    return input(text)

def get_game_board_string(cells: list[list[str]]) -> str:
    game_board_string = f"{'-' * len(cells)*2}-\n"

    for row in cells:
        game_board_string += f"|{'|'.join(row)}|\n"
        game_board_string += f"{'-' * len(cells)*2}-\n"

    return game_board_string