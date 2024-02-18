class Case:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.checked = False
        self.piece = "None"
        self.selected = False
        self.color = "white" if (row + col) % 2 == 0 else "black"
        self.reset = False

    def __str__(self):
        return f"({self.row}, {self.col})"


class Player:
    def __init__(self, name):
        self.name = name
        self.piece_selected = False
        self.clicked = False

    def __repr__(self):
        return f'<User {self.name}>'
