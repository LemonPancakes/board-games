class Game:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.new_game()

    def __str__(self):
        raise NotImplementedError("__str__() not implemented")

    def new_game(self):
        raise NotImplementedError("new_game() not implemented")

    def make_move(self, move):
        raise NotImplementedError("make_move() not implemented")

    def check_win(self):
        raise NotImplementedError("check_win() not implemented")
