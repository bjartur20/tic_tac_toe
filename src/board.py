class GameBoard:
    def setup_game_board(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def __str__(self) -> str:
        ret = f"{'-' * len(self.cells*2)}-\n"

        for row in self.cells:
            ret += f"|{'|'.join(row)}|\n"
            ret += f"{'-' * len(self.cells*2)}-\n"

        return ret

    @property
    def is_full(self) -> bool:
        return all([cell != " " for row in self.cells for cell in row])

    def place_symbol(self, symbol: str, index: int):
        self.cells[index // 3][index % 3] = symbol
    
    def is_cell_empty(self, index: int) -> bool:
        return self.cells[index // 3][index % 3] == " "

    def contains_winner(self) -> str | None:
        # TODO: Might be able to refactor this function

        for i in range(len(self.cells) - 1):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] != " ":
                return self.cells[i][0]
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] != " ":
                return self.cells[0][i]
        
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != " ":
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != " ":
            return self.cells[0][2]
