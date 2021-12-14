import numpy as np

def has_duplicates(list_check, list_check_len=False):
    # Check if list has duplicated entries.
    list_len = list_check_len
    if not list_len:
        list_len = len(list)
    for i in range(list_len):
            for j in range (i+1, list_len):
                if list_check[i]==list_check[j]:
                    return True
    return False

def matrix_to_list(matrix):
    result = []
    for i in range (len(matrix)):
        result += matrix[i]
    return result


class Pydoku:

    def __init__(self, game_array):
        # game: a (9,9) numpy array with entries from 0 to 9, where 0 means empty entry.
        self._game = game_array.tolist()
        self._game_len = len(game_array)

    def get_string_sudoku(self): #TODO
        # return formated string representing sudoku game
        pass

    def get_game_array(self):
        return np.array(self._game)

    def get_game(self):
        return self._game

    def get_game_len(self):
        return self._game_len

    def get_entry(self, i, j):
        return self._game[i][j]

    def get_row(self, k):
        return self._game[k]

    def get_column(self, k):
        column = []
        for i in range(self._game_len):
            column.append(self._game[i][k])
        return column

    def get_square(self, k):
        square = [[],[],[]]
        for i in range(self._game_len):
            square[i//3].append(self._game[(3*(k//3)) + i//3][(3*(k%3))+(i%3)])
        return square

    def set_game(self, game_array):
        self._game = game_array.tolist()
        self._game_len = len(self._game)

    def set_game_list(self, game):
        self._game = game
        self._game_len = len(game)

    def set_game_len(self, game_len):
        self._game_len = game_len

    def set_entry(self, i, j, new_entry):
        self._game[i][j] = new_entry

    def set_row(self, k, new_row):
        self._game[k] = new_row

    def set_column(self, k, new_column):
        for i in range(self._game_len):
            self._game[k][i] = new_column[i]

    def set_square(self, k, new_square): #TODO
        pass

    def is_complete(self):
        for i in range(self._game_len):
            if 0 in self._game[i]:
                return False
        return True

    def is_solved(self):
        if self.is_complete():
            if self.is_solved_rows() and self.is_solved_columns() and self.is_solved_squares():
                return True
        return False

    def is_solved_rows(self):
        for i in range(self._game_len):
            if not self.is_solved_row(i):
                return False
        return True

    def is_solved_row(self, k):
        row = self.get_row(k)
        return self._is_solved_list(row)

    def is_solved_columns(self):
        for i in range(self._game_len):
            if not self.is_solved_column(i):
                return False
        return True

    def is_solved_column(self, k):
        column = self.get_column(k)
        return self._is_solved_list(column)

    def is_solved_squares(self):
        for i in range(self._game_len):
            if not self.is_solved_square(i):
                return False
        return True

    def is_solved_square(self, k):
        square = self.get_square(k)
        return self._is_solved_list(matrix_to_list(square))

    def _is_solved_list(self, list_check):
        if 0 in list_check:
            return False
        if has_duplicates(list_check, self._game_len):
            return False
        if not self._is_list_valid(list_check):
            return False
        return True

    def _is_list_valid(self, list_check):
        for i in range(self._game_len):
            if list_check[i]>self._game_len or list_check[i]<0:
                return False
        return True