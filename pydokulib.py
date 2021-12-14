import numpy as np

class pydoku:
    
    def __init__(self, game):
        # game: a (9,9) numpy array with entries from 0 to 9, where 0 means empty entry.
        self._game_array = game
        self._game = game.tolist()
        self._game_len = len(game)
    
    def is_complete(self):
        for i in range(self._game_len):
            if 0 in self._game[i]:
                return False
        return True
    
    def is_solved(self):
        if self.is_complete():
            if self._is_solved_rows() and self._is_solved_columns() and self._is_solved_squares():
                return True
        return False
    
    def _is_solved_rows(self):
        for i in range(self._game_len):
            if not self._is_solved_row(i):
                return False
        return True
    
    def _is_solved_row(self, k):
        if 0 in self._game[k]:
            return False
        for i in range(self._game_len):
            for j in range (i+1, self._game_len):
                if self._game[k][i]==self._game[k][j]:
                    return False
        
        return True
    
    def _is_solved_columns(self):
        for i in range(self._game_len):
            if not self._is_solved_column(i):
                return False
        return True
    
    def _is_solved_column(self, k):
        column = []
        for i in range(self._game_len):
            column.append(self._game[i][k])
        
        if 0 in column:
            return False
        for i in range(self._game_len):
            for j in range (i+1, self._game_len):
                if column[i]==column[j]:
                    return False
        
        return True
    
    def _is_solved_squares(self):
        for i in range(self._game_len):
            if not self._is_solved_square(i):
                return False
        return True
    
    def _is_solved_square(self, k):
        square = []
        for i in range(self._game_len):
            square.append(self._game[(3*(k//3)) + i//3][(3*(k%3))+(i%3)])

        if 0 in square:
            return False
        
        for i in range(self._game_len):
            for j in range(i+1, self._game_len):
                if square[i]==square[j]:
                    return False
        
        return True