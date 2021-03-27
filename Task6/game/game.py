import random

from util.misc import Misc


class Game:
    def __init__(self, difficulty="Легкий"):
        self.row = 0
        self.col = 0
        self.game_matrix = []
        self.ui = None
        self.length = 3
        self.init_new_game_using_difficulty(difficulty)

    def init_new_game_using_difficulty(self, difficulty_text):
        amount = 0
        self.game_matrix = []
        if difficulty_text == "Легкий":
            amount = 16
            for i in range(0, 5):
                self.game_matrix.append([])
                for j in range(0, 5):
                    self.game_matrix[i].append(0)

        elif difficulty_text == "Средний":
            amount = 32
            for i in range(0, 7):
                self.game_matrix.append([])
                for j in range(0, 7):
                    self.game_matrix[i].append(0)
        elif difficulty_text == "Сложный":
            amount = 64
            for i in range(0, 9):
                self.game_matrix.append([])
                for j in range(0, 9):
                    self.game_matrix[i].append(0)
        self.generate_random_start(amount)

    def generate_random_start(self, amount):
        for i in range(0, len(self.game_matrix)):
            for j in range(3, len(self.game_matrix[0])):
                self.game_matrix[i][j] = 1
        for i in range(0, amount):
            self.rotate_game_section(self.rand_row, self.rand_col, 3)

    @property
    def rand_row(self):
        return random.randint(0, len(self.game_matrix) - 3)

    @property
    def rand_col(self):
        return random.randint(0, len(self.game_matrix[0]) - 3)

    def rotate_game_section(self, row, col, length):
        section = []
        for i in range(0, length):
            section.append([])
            for j in range(0, length):
                section[i].append(self.game_matrix[row + i][col + j])
        section = tuple(zip(*section[::-1]))
        for i in range(0, len(section)):
            for j in range(0, len(section[i])):
                self.game_matrix[row + i][col + j] = section[i][j]

    def try_to_move_to_pos(self, row, col):
        self.row = Misc.clamp(row, 0, len(self.game_matrix) - self.length)
        self.col = Misc.clamp(col, 0, len(self.game_matrix[0]) - self.length)
