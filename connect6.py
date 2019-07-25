from game import Game
import warnings


class Connect6(Game):
    def __init__(self):
        self.boardsize = 19
        super().__init__(self.boardsize)

    def new_game(self):
        self.board = [[0 for _ in range(self.boardsize)] for _ in range(self.boardsize)]
        self.current_player = 1
        self.first_move = False
        self.finished = False

    def make_move(self, move):
        if self.finished:
            warnings.warn("game is finished")

        r, c = move
        if self.board[r][c] != 0:
            warnings.warn("space is taken")

        self.board[r][c] = self.current_player
        if self.check_win(move, self.current_player):
            return

        if not self.first_move:
            self.current_player = 3 - self.current_player

        self.first_move = not self.first_move

    def check_win(self, last_move, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for direction in directions:
            curr_length = 1
            x, y = last_move
            x += direction[0]
            y += direction[1]
            while curr_length < 6 and x < 19 and x >= 0 and y < 19 and y >= 0 and player == self.board[x][y]:
                x += direction[0]
                y += direction[1]
                curr_length += 1
