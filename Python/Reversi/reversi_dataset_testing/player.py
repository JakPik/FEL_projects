MATRIX_SIZE = 8

class MyPlayer:
    """Player"""
    def __init__(self, my_color = 0,opponent_color = 0):
        self.name = "Jakub Pikal"
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.row_coord = 0
        self.column_coord = 0
        self.game_matrix = self.create_matrix()
        self.move_matrix = self.create_matrix()
        pass

    def create_matrix(self):
        return [[0 for _ in range (MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    def clear_move_matrix(self):
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                self.move_matrix [r][c] = 0
        return 0

    def move(self, board):
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                self.game_matrix [r][c] = board [r][c]
                if(self.game_matrix [r][c] == self.my_color):
                    self.near_check(r,c)
        self.play_move()
        return (self.row_coord, self.column_coord)
    
    def check_bounds(self, row, column, skip):
        if ((row or column) < 0 or (row or column) > 7):
            skip = True
        else:
            skip = False
        return skip

    def near_check(self, row, column):
        self.clear_move_matrix()
        for r in range(-1,1):
            for c in range(-1,1):
                if((r == 0 and c == 0) or self.check_bounds(row + r, column + c) == True):
                    break
                if(self.game_matrix[row + r][column + c] == self.opponent_color):
                    self.line_check_set(row + r, column + c, r, c)
        return 0

    def line_check_set(self, row, column, row_coef, column_coef):
        count = 1
        while(self.game_matrix[row + row_coef*count][column + column_coef*count] == self.opponent_color):
            count += 1
        if(self.game_matrix[row + row_coef*count][column + column_coef*count] == self.my_color):
            self.move_matrix[row + row_coef*count][column + column_coef*count] = 0
            return 0
        self.move_matrix[row + row_coef*count][column + column_coef*count] += count
        return 0
    
    def play_move(self):
        max_value = 0
        max_value_optimal = 0
        row_idx_optimal = -1
        column_idx_optimal = -1
        row_idx = -1
        column_idx = -1
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                if(self.move_matrix [r][c] > max_value and 1 != r != 6 and 1 != r != 6):
                    max_value = self.move_matrix [r][c]
                    max_value_optimal = max_value
                    row_idx_optimal = r
                    column_idx_optimal = c
                elif(self.move_matrix [r][c] > max_value):
                    max_value = self.move_matrix [r][c]
                    row_idx = r
                    column_idx = c
        if(max_value_optimal >= max_value):
            self.row_coord = row_idx_optimal
            self.column_coord = column_idx_optimal
        elif(row_idx_optimal != -1 and column_idx_optimal != -1):
            self.row_coord = row_idx_optimal
            self.column_coord = column_idx_optimal
        else:
            self.row_coord = row_idx
            self.column_coord = column_idx
        return 0
    