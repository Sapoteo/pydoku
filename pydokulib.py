'''
Python module for checking, solving and generating sudoku puzzles.

author: Sapoteo
'''

# TODO: module and methods docstrings

import numpy as np

def has_duplicates(list_check, max_check_index=False):
    '''
    Check if a list has duplicated entries.
    ---------------------------------------
    list_check: list that will be checked for duplicates.

    max_check_index: greatest index that will be considered
    when checking for duplicates.
    '''
    list_len = max_check_index
    if not list_len:
        list_len = len(list)
    for i in range(list_len):
        for j in range (i+1, list_len):
            if list_check[i]==list_check[j]:
                return True
    return False

def matrix_to_list(matrix):
    '''
    Convert matrix to a list by appending its rows from first to last.
    ------------------------------------------------------------------
    matrix: list with sublists that will be appended into one.
    '''
    result = []
    for row in matrix:
        result += row
    return result

def generate_possible_lists(list_len, upper_bound=9, lower_bound=1, allowed_values = None):
    '''
    generate_possible_lists(list_len, upper_bound = 9, lower_bound = 1, allowed_values = None)

    Returns a list with all possible lists of size list_len

    Parameters
    ----------
    list_len: int
        Integer that gives the generated lists sizes.
    upper_bound: int
        TODO: descriptions
    lower_bound: int
    allowed_vallues: list
    '''

    possible_lists = []
    if allowed_values is None:
        values = range(lower_bound,upper_bound+1)
    else:
        values = allowed_values

    values_len = len(values)

    for i in range(values_len**list_len):
        temp_list = []
        for j in range(list_len):
            temp_list.append(values[(i//(values_len**j))%values_len]) # TODO fix index
        possible_lists.append(temp_list)

    return possible_lists

class Pydoku:

    '''
    Pydoku class holds a sudoku game and provide methods to modify its entries,
    check solutions, solve and generate new games.
    '''

    def __init__(self, game_array):
        '''
        Standard __init__ method.
        -------------------------
        game: a (9,9) numpy array with entries from 0 to 9, where 0 means empty entry in sudoku.
        '''
        self._game = game_array.tolist()
        self._game_len = len(game_array)

    def get_string_sudoku(self): #TODO
        '''
        Return formated string representing sudoku game.
        '''

    def get_game_array(self):
        '''
        Returns game board in numpy array type.
        '''
        return np.array(self._game)

    def get_game(self):
        '''
        Returns game board in list type.
        '''
        return self._game

    def get_game_len(self):
        '''
        Returns game length (number of rows in game board).
        '''
        # Ps.: will be usefull when considering 16x16 or other sizes of sudoku.
        return self._game_len

    def get_entry(self, i, j):
        '''
        Returns the entry [i][j] from game matrix.
        '''
        return self._game[i][j]

    def get_row(self, k):
        '''
        Returns row [k] from game matrix.
        '''
        return self._game[k]

    def get_column(self, k):
        '''
        Returns a list with the [k] term from each row of the game matrix.
        '''
        column = []
        for i in range(self._game_len):
            column.append(self._game[i][k])
        return column

    def get_square(self, k):
        '''
        Returns the 3x3 submatrix from game matrix.
        The submatrices are taken from 0 to 8, starting the count
        from up left.
        '''
        square = [[],[],[]]
        for i in range(self._game_len):
            square[i//3].append(self._game[(3*(k//3)) + i//3][(3*(k%3))+(i%3)])
        return square

    def set_game(self, game_array):
        '''
        Set the game matrix to a new numpy array, and update the
        game_len accordingly.
        ----------------------------------------------------
        game_array: new sudoku game in numpy array type.
        '''
        self._game = game_array.tolist()
        self._game_len = len(self._game)

    def set_game_list(self, game):
        '''
        Set the game matrix to a new list, and update the
        game_len accordingly.
        ----------------------------------------------------
        game: new sudoku game in list type.
        '''
        self._game = game
        self._game_len = len(game)

    def set_game_len(self, game_len):
        '''
        well, maybe it's useless. #TODO: really??
        '''
        self._game_len = game_len

    def set_entry(self, i, j, new_entry):
        '''
        Set the game matrix [i][j] entry to a new value.
        ------------------------------------------------
        new_entry: new value that will be assigned to matrix [i][j] entry.
        '''
        self._game[i][j] = new_entry

    def set_row(self, k, new_row):
        '''
        Set the [k] row of game matrix to a new list.
        ---------------------------------------------
        new_row: new list that will be assigned to matrix [k] row.
        '''
        self._game[k] = new_row

    def set_column(self, k, new_column):
        '''
        Set the [k] column (i.e, the list of [k] entry of all rows) of game matrix to a new list.
        ---------------------------------------------
        new_column: new list that will be assigned to matrix [k] column.
        '''
        for i in range(self._game_len):
            self._game[k][i] = new_column[i]

    def set_square(self, k, new_square): #TODO decidir como receber a entrada tambem
        '''
        Set the [k] 3x3 submatrix of game matrix to a new submatrix.
        ---------------------------------------------
        new_square: new list that will be assigned to matrix [k] submatrix.
        '''

    def is_complete(self):
        '''
        Returns True if no entry of the matrix is empty (0 value).
        Returns false otherwise.
        '''
        for i in range(self._game_len):
            if 0 in self._game[i]:
                return False
        return True

    def is_solved(self):
        '''
        Returns True if the game is complete and is a valid sudoku game.
        Returns false otherwise.
        '''
        if self.is_complete():
            if self.is_solved_rows() and self.is_solved_columns() and self.is_solved_squares():
                return True
        return False

    def is_solved_rows(self):
        '''
        Returns True if all rows are complete and are valid sudoku rows.
        Returns false otherwise.
        '''
        for i in range(self._game_len):
            if not self.is_solved_row(i):
                return False
        return True

    def is_solved_row(self, k):
        '''
        Returns True if the [k] row of game matrix is complete and is a valid sudoku row.
        Returns false otherwise.
        '''
        row = self.get_row(k)
        return self._is_solved_list(row)

    def is_solved_columns(self):
        '''
        Returns True if all columns are complete and are valid sudoku columns.
        Returns false otherwise.
        '''
        for i in range(self._game_len):
            if not self.is_solved_column(i):
                return False
        return True

    def is_solved_column(self, k):
        '''
        Returns True if the [k] column of game matrix is complete and is a valid sudoku column.
        Returns false otherwise.
        '''
        column = self.get_column(k)
        return self._is_solved_list(column)

    def is_solved_squares(self):
        '''
        Returns True if all 3x3 squares are complete and are valid sudoku squares.
        Returns false otherwise.
        '''
        for i in range(self._game_len):
            if not self.is_solved_square(i):
                return False
        return True

    def is_solved_square(self, k):
        '''
        Returns True if the [k] 3x3 square is complete and is a valid sudoku square.
        Returns false otherwise.
        '''
        square = self.get_square(k)
        return self._is_solved_list(matrix_to_list(square))

    def _is_solved_list(self, list_check):
        '''
        Returns True if a list is complete and is a valid sudoku row or column.
        Returns false otherwise.
        -----------------------------------------------------------------------
        list_check: list to be checked.
        '''
        if 0 in list_check:
            return False
        if has_duplicates(list_check, self._game_len):
            return False
        if not self._is_list_in_range(list_check):
            return False
        return True

    def _is_list_in_range(self, list_check):
        '''
        Check if the list entries are in range(9).
        ------------------------------------------
        list_check: list to be checked.
        '''
        for i in range(self._game_len):
            if list_check[i]>self._game_len or list_check[i]<0:
                return False
        return True

    def _count_empty_entries(self):
        '''
        Return the number of empty entries.
        '''
        n_zeros = 0
        for i in matrix_to_list(self.get_game()):
            if i == 0:
                n_zeros += 1

        return n_zeros

    def set_empty_entries(self, new_entries):
        '''
        Set the empty entries to values in new_entries list.
        '''

        if self._count_empty_entries() > len(new_entries): # TODO: ajeita isso por favor.
            raise Exception("set_empty_entries error: more empty entries than new_entries gave.")

        new_entries_index = 0
        for (row_index, new_row) in enumerate(self.get_game()):
            for (value_index, value) in enumerate(new_row):
                if value == 0:
                    # FIXME: prints debuging
                    # print('\n\nEm set_empty_entries')
                    # print(f"value_index = {value_index}")
                    # print(f"new_entries_index = {new_entries_index}")
                    # print(f"new_row len = {len(new_row)}")
                    # print(f'new_entries len = {len(new_entries)}\n\n')
                    # Resultado: parece que new_entries tem tamanho apenas 1. Por que?
                    new_row[value_index] = new_entries[new_entries_index]
                    new_entries_index += 1
            self.set_row(row_index, new_row)

    def brute_solve(self):
        '''
        Solve sudoku by brute force, testing all possibilities.
        Returns the number of solutions found.
        '''
        n_solutions = 0
        n_zeros = self._count_empty_entries()
        game_solution = None

        # Generate all possible lists with n_zeros length and entries from 1 to 9.
        # FIXME: outros prints pra testar bug
        # print(f'\n n_zeros = {n_zeros}')
        # print(f'game_len = {self.get_game_len()}')
        possible_solutions = generate_possible_lists(n_zeros, self.get_game_len())
        for solution in possible_solutions:
            # FIXME: testando possible_solutions
            # print('\n\nEm brute_solve')
            # print(f'possible solutions len = {len(possible_solutions)}')
            # print(f'solution = {solution}\n\n')
            game_fill = Pydoku(self.get_game_array())
            game_fill.set_empty_entries(solution)
            if game_fill.is_solved():
                n_solutions += 1
                game_solution = game_fill.get_game()
        if game_solution is not None:
            self.set_game_list(game_solution)
        return n_solutions
